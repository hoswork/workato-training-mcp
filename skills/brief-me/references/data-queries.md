# Enterprise Data (Snowflake) — Footprint Queries

These queries run through the **Enterprise Data by Workato MCP** connector against the `DATA_GENIE.WORKATO_ANALYTICS` Snowflake warehouse. The connector does **not** accept raw ad-hoc SQL as a first move — it uses a guided 5-step semantic-layer flow. Follow it:

1. **`start_session`** → returns `session_id` + `user_email` (required by every later call).
2. **`get_analyst_context`** → loads analyst instructions / warehouse context.
3. **`get_semantic_layer_index`** → search with the question (e.g. "Top connectors and active recipes by job volume for account [Account]"); returns an `index_key`. Call again per missing data domain if needed.
4. **`get_semantic_models`** (with `index_key`) → loads table/metric/verified-query definitions. Prefer verified queries → metrics → relationships → tables.
5. **`execute_sql_query`** → run the SQL, setting `sql_generation_type` (`VQR` / `VQR_ADAPTED` / `METRIC_BASED` / `LLM_GENERATED`).

**Account resolution (do this first):** resolve the exact account before footprint queries —
```sql
SELECT DISTINCT account_name FROM DATA_GENIE.WORKATO_ANALYTICS.DIM_ACCOUNT WHERE account_name ILIKE '%[account]%'
```
Check for Embedded/regional variants (e.g. "[Name] - Embedded", "[Name] Japan"). Use the resolved `account_name` in the queries below.

> The SQL below is a **starting point** expressing the footprint intent (top connectors by jobs, by active recipes, top recipe per connector, recipe metadata + job stats). Table/column names can drift — let `get_semantic_models` confirm the correct objects (e.g. `pud_task_daily_agg`, `dim_recipe`, `consumption_usage_fact`) and adapt. If a verified query already answers the intent, use it (`VQR`).

---

# Data Genie SQL Queries

Replace `[account]` with the exact lowercase account name from Step 1.

---

## Query A — Top 25 Connectors by Total Jobs (all recipe statuses)

```sql
SELECT
    app.value::STRING AS connector_name,
    COUNT(DISTINCT t.recipe_id) AS total_recipes,
    SUM(t.recipe_task_count) AS total_tasks,
    SUM(t.job_count) AS total_jobs,
    SUM(t.successful_job_count) AS successful_jobs,
    SUM(t.failed_job_count) AS failed_jobs,
    ROUND(100.0 * SUM(t.successful_job_count) / NULLIF(SUM(t.job_count), 0), 1) AS success_rate_pct,
    MIN(t.entry_date) AS first_seen,
    MAX(t.entry_date) AS last_seen
FROM data_genie.workato_analytics.pud_task_daily_agg t,
    LATERAL FLATTEN(input => t.applications_list) app
WHERE LOWER(t.account_name) LIKE '%[account]%'
  AND t.is_excluded_workspace = FALSE
GROUP BY connector_name
ORDER BY total_jobs DESC
LIMIT 25
```

---

## Query B — Top 25 Connectors by Active Recipe Count

```sql
SELECT
    app.value::STRING AS connector_name,
    COUNT(DISTINCT t.recipe_id) AS total_recipes,
    SUM(t.recipe_task_count) AS total_tasks,
    SUM(t.job_count) AS total_jobs,
    SUM(t.successful_job_count) AS successful_jobs,
    SUM(t.failed_job_count) AS failed_jobs,
    ROUND(100.0 * SUM(t.successful_job_count) / NULLIF(SUM(t.job_count), 0), 1) AS success_rate_pct,
    MIN(t.entry_date) AS first_seen,
    MAX(t.entry_date) AS last_seen
FROM data_genie.workato_analytics.pud_task_daily_agg t,
    LATERAL FLATTEN(input => t.applications_list) app
WHERE LOWER(t.account_name) LIKE '%[account]%'
  AND t.is_excluded_workspace = FALSE
  AND t.recipe_status = 'Active'
GROUP BY connector_name
ORDER BY total_recipes DESC
LIMIT 25
```

---

## Query C — Top Active Recipe per Connector (top 10 connectors by jobs)

Replace `[top 10 connector names]` with a quoted IN list from Query A results.

```sql
SELECT
    app.value::STRING AS connector_name,
    t.recipe_id,
    t.recipe_name,
    SUM(t.job_count) AS total_jobs,
    SUM(t.successful_job_count) AS successful_jobs,
    ROUND(100.0 * SUM(t.successful_job_count) / NULLIF(SUM(t.job_count), 0), 1) AS success_rate_pct,
    MIN(t.entry_date) AS first_seen,
    MAX(t.entry_date) AS last_seen
FROM data_genie.workato_analytics.pud_task_daily_agg t,
    LATERAL FLATTEN(input => t.applications_list) app
WHERE LOWER(t.account_name) LIKE '%[account]%'
  AND t.is_excluded_workspace = FALSE
  AND t.recipe_status = 'Active'
  AND app.value::STRING IN ([top 10 connector names from Query A])
GROUP BY connector_name, t.recipe_id, t.recipe_name
QUALIFY ROW_NUMBER() OVER (PARTITION BY connector_name ORDER BY SUM(t.job_count) DESC) = 1
ORDER BY total_jobs DESC
```

> Multiple connectors often share the same top recipe. Deduplicate recipe IDs before Queries D and E.

---

## Query D — Full Metadata for Unique Active Recipes

Replace `[recipe IDs]` with deduplicated list from Query C.

```sql
SELECT DISTINCT
    recipe_id,
    recipe_name,
    trigger_app,
    applications_list,
    is_ai,
    recipe_status,
    environment_type,
    folder_path,
    workspace_id,
    recipe_created_date,
    is_function,
    is_automation,
    is_integration,
    is_etl,
    has_function
FROM data_genie.workato_analytics.pud_task_daily_agg
WHERE LOWER(account_name) LIKE '%[account]%'
  AND is_excluded_workspace = FALSE
  AND recipe_id IN ([comma-separated unique recipe IDs from Query C])
```

---

## Query E — Job Counts and Date Ranges per Recipe

```sql
SELECT
    recipe_id,
    recipe_name,
    SUM(job_count) AS total_jobs,
    SUM(successful_job_count) AS successful_jobs,
    SUM(failed_job_count) AS failed_jobs,
    ROUND(100.0 * SUM(successful_job_count) / NULLIF(SUM(job_count), 0), 1) AS success_rate_pct,
    MIN(entry_date) AS first_run,
    MAX(entry_date) AS last_run
FROM data_genie.workato_analytics.pud_task_daily_agg
WHERE LOWER(account_name) LIKE '%[account]%'
  AND is_excluded_workspace = FALSE
  AND recipe_id IN ([comma-separated unique recipe IDs from Query C])
GROUP BY recipe_id, recipe_name
ORDER BY total_jobs DESC
```

---

## Salesforce Queries

### Account Profile

```soql
SELECT Id, Name, Current_ARR_USD__c, Renewal_Date__c, Subscription_Start_Date__c,
       NumberOfEmployees, Industry, Account_Executive_hidden__c, Expansion_CSM_Name_hidden__c,
       At_Risk_Status__c, Adoption_IT__c, Adoption_HR__c, Adoption_GTM__c,
       Platform_Edition__c, Total_Active_Recipes__c, Total_Billable_Recipes__c,
       No_of_Workato_Users__c, No_of_Certified_Students__c,
       Customer_Tier__c, Segment__c, BillingAddress, Website,
       Description, About_the_Customer__c, Account_Strategy__c,
       Goals_KPIs__c, Future_Expansion_Opportunities__c
FROM Account
WHERE Name LIKE '%[Account]%'
  AND Type = 'Customer'
```

### Contacts

```soql
SELECT Id, Name, Title, Email, Phone, Department
FROM Contact
WHERE AccountId = '[AccountId]'
ORDER BY LastModifiedDate DESC
```

### Opportunity History

```soql
SELECT Id, Name, StageName, Amount, CloseDate, Type, LeadSource, Description
FROM Opportunity
WHERE AccountId = '[AccountId]'
ORDER BY CloseDate DESC
```
