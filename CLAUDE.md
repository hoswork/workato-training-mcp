# workato-qr — Claude context

QR code generator with two deployment targets: a local Python CLI (`cli/`) and a Workato Skill + MCP server (`workato/`).

## Repo structure

```
workato-qr/
  cli/           — standalone Python CLI using qrcode[pil] + Pillow
  workato/       — RCLM project (push/pull via Workato platform CLI)
    workato-qr/
      generate_qr_code.recipe.json       — Workato Skill trigger + py_eval
      generate_qr_code.agentic_skill.json
      workato_qr_mcp.mcp_server.json
      project.json
```

## Workato platform CLI

### Setup (first time in a new session)
The CLI workspace is already initialized. Profile is `trial`.

```bash
cd ~/code/workato-qr/workato
workato workspace     # confirms trial profile + project 28820
```

If the workspace is not initialized:
```bash
AUTH_TOKEN=$(jq -r '.mcpServers["workato-dev-api"].env.AUTH_HEADER' ~/.mcp.json | sed 's/Bearer //')
workato init \
  --profile trial \
  --region custom \
  --api-url https://app.trial.workato.com \
  --api-token "$AUTH_TOKEN" \
  --project-id 28820 \
  --non-interactive
```

### Push (deploy local → cloud)
```bash
cd ~/code/workato-qr/workato
workato push --restart-recipes
```

**`workato push` is authoritative.** It overwrites the cloud with local file values — including the Genie/MCP server config. Always edit local JSON files, push, then pull to verify.

### Pull (sync cloud → local)
```bash
cd ~/code/workato-qr/workato
workato pull
```

Always pull after making changes in the Workato UI so the local files stay in sync.

### Pushing the MCP server
The MCP server config is in `workato/workato-qr/workato_qr_mcp.mcp_server.json`. It is included in every `workato push`. After pushing, the MCP server is live at the URL in that file.

To verify the MCP server is working:
```bash
curl -sk -X POST "https://2581.apim.mcp.trial.workato.com?wkt_token=<token>" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/list","params":{}}'
```

## Authoritative facts

| Resource | Value |
|---|---|
| Trial workspace | id `2100000234` |
| Project | `workato-qr` id `28820` |
| Folder | id `42011` |
| Recipe | `generate_qr_code` id `277230` |
| Skill | id `skl-AaXQmwN6-MBemcL-AB` |
| MCP server | id `mcps-AaXQnHFM-aLA-AB` |
| MCP URL | `https://2581.apim.mcp.trial.workato.com` |
| Dev API auth | `jq -r '.mcpServers["workato-dev-api"].env.AUTH_HEADER' ~/.mcp.json` |

The MCP server token (wkt_token) is in `workato/workato-qr/workato_qr_mcp.mcp_server.json`. **Do not hardcode it in code** — read it from the file.

## Dev API hints

Auth pattern:
```bash
AUTH=$(jq -r '.mcpServers["workato-dev-api"].env.AUTH_HEADER' ~/.mcp.json)
curl -s -H "Authorization: $AUTH" "https://app.trial.workato.com/api/..."
```

Useful endpoints:
```bash
# Check recipe status
curl -s -H "Authorization: $AUTH" "https://app.trial.workato.com/api/recipes/277230" | jq '{running, version_no}'

# Start/stop recipe
curl -s -X PUT -H "Authorization: $AUTH" "https://app.trial.workato.com/api/recipes/277230/start"

# Get MCP server details
curl -s -H "Authorization: $AUTH" "https://app.trial.workato.com/api/mcp/mcp_servers/mcps-AaXQnHFM-aLA-AB" | jq '.data | {name, mcp_url, tools_count}'

# Re-assign skill to MCP server (if tools_count drops to 0)
curl -s -X POST -H "Authorization: $AUTH" -H "Content-Type: application/json" \
  -d '{"tools":[{"id":"skl-AaXQmwN6-MBemcL-AB","trigger_application":"workato_skill"}]}' \
  "https://app.trial.workato.com/api/mcp/mcp_servers/mcps-AaXQnHFM-aLA-AB/assign_tools"
```

**Avoid `mcp__workato-dev-api__post_api_collections_api_endpoints`** — it has a broken JSON Schema that poisons the MCP tool list if ToolSearched.

## Chrome DevTools hints

Use Chrome DevTools MCP (not Playwright) for browser interactions with the Workato UI.

To test the recipe via Agent Studio:
1. Navigate to `https://app.trial.workato.com/recipes/277230`
2. Use the recipe's test/run UI to trigger a test job with `{"url": "https://workato.com"}`
3. Check the job output for `image_base64`

To test via Workato GO (if a Genie is wired to the skill):
- Navigate to `https://hosman-demo.workato-dev.ai`

Chrome DevTools process: `npx chrome-devtools-mcp@1.2.0` — kill any existing sessions with `pkill -f chrome-devtools-mcp` first.

## Recipe implementation notes

**Python stdlib only.** The `py_eval` step in Workato does not have `qrcode` or `Pillow`. The recipe calls `api.qrserver.com` using `urllib.request` (stdlib).

```python
import urllib.request, urllib.parse, base64
# url → api.qrserver.com → PNG bytes → base64
```

The `cli/` version uses `qrcode[pil]` + `Pillow` for local use where libraries are available.

## MCP response shape

The Workato MCP server wraps the skill output in an extra layer:

```json
{
  "result": {
    "content": [{
      "type": "text",
      "text": "{\"result\": {\"image_base64\": \"...\", \"mime_type\": \"image/png\", ...}}"
    }]
  }
}
```

To extract the image:
```python
import json
data = json.loads(response["result"]["content"][0]["text"])["result"]
image_bytes = base64.b64decode(data["image_base64"])
```

## Known landmines

- **`workato push` overwrites MCP token** — the `wkt_token` in `workato_qr_mcp.mcp_server.json` is managed by Workato. After a push, pull to get the current token value.
- **Recipe must be running** before the MCP tool can be invoked. Check with `curl .../api/recipes/277230 | jq .running`.
- **Workato GO paperclip disappears** after a push while Workato GO is open — refresh the page.
- **SSL cert on this machine** — `urllib` calls to external URLs fail locally due to Zscaler. Use `curl -sk` for local tests. Workato's Python sandbox runs server-side and has no SSL proxy issues.
