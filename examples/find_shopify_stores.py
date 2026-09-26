"""Lead generation: keep only the websites that use a given technology (e.g. Shopify, Klarna, HubSpot)."""
import os

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("jesting_grass/tech-stack-detector").call(run_input={
    "domains": ["allbirds.com", "gymshark.com", "klarna.com", "hubspot.com", "ikea.com"],
    "onlyDomainsUsing": ["Shopify"],
})
for row in client.dataset(run.default_dataset_id).iterate_items():
    if "error" not in row:
        print(row["domain"], "uses", row["matchedTechnologies"], "| payments:", row["payments"] or "-")
