"""Tech stack of many websites -> CSV (CMS, ecommerce, payments, analytics, CRM, hosting...).

pip install "apify-client>=3"
export APIFY_TOKEN=...   # free account: https://console.apify.com
"""
import csv
import os

from apify_client import ApifyClient

DOMAINS = ["allbirds.com", "gymshark.com", "klarna.com", "hubspot.com", "ikea.com"]
COLUMNS = ["domain", "technologyCount", "cms", "ecommerce", "payments", "analytics",
           "marketingAutomation", "crm", "hosting", "cdn", "technologyNames"]

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("jesting_grass/tech-stack-detector").call(run_input={"domains": DOMAINS})

with open("tech_stacks.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=COLUMNS, extrasaction="ignore")
    writer.writeheader()
    for row in client.dataset(run.default_dataset_id).iterate_items():
        if "error" not in row:
            writer.writerow(row)
            print(f'{row["domain"]:<14} CMS: {row["cms"] or "-":<22} payments: {row["payments"] or "-"}')
print("Saved tech_stacks.csv")
