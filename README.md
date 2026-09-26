# BuiltWith & Wappalyzer alternative — bulk tech stack lookup API (Python, Node.js, cURL)

Find out **what any website is built with, in bulk**: CMS, ecommerce platform, payment providers, analytics, CRM, marketing automation, hosting, CDN and frameworks — as JSON or a CSV-ready table. Pay per website, **no $250–$295/month subscription**.

It uses the [**Tech Stack Detector**](https://apify.com/jesting_grass/tech-stack-detector) on Apify: up to 20 technologies per site with categories, from a commercial technographics provider. Invalid, offline or undetectable sites are not charged.

## Quick start (Python)

```bash
pip install "apify-client>=3"
export APIFY_TOKEN=your_token   # free account at https://console.apify.com
```

```python
from apify_client import ApifyClient

client = ApifyClient("YOUR_APIFY_TOKEN")
run = client.actor("jesting_grass/tech-stack-detector").call(run_input={
    "domains": ["allbirds.com", "gymshark.com", "klarna.com", "hubspot.com", "ikea.com"],
})
for row in client.dataset(run.default_dataset_id).iterate_items():
    print(row["domain"], "|", row.get("cms"), "|", row.get("payments"))
```

Real output (September 2026):

```
klarna.com     CMS: Contentful             payments: Klarna Checkout
gymshark.com   CMS: Contentful, Shopify    payments: -
allbirds.com   CMS: Shopify                payments: Stripe
ikea.com       CMS: WordPress              payments: -
hubspot.com    CMS: HubSpot CMS Hub        payments: -
```

## Examples

| File | What it does |
|---|---|
| [`bulk_lookup_to_csv.py`](examples/bulk_lookup_to_csv.py) | Tech stack for a list of domains → `tech_stacks.csv` |
| [`find_shopify_stores.py`](examples/find_shopify_stores.py) | Lead generation: keep only sites using Shopify (or HubSpot, Klarna, WordPress…) |
| [`node.js`](examples/node.js) | Same in Node.js |
| [`curl.sh`](examples/curl.sh) | One HTTP call, JSON back |

## Output fields

| Field | Example |
|---|---|
| `domain` | `allbirds.com` |
| `technologyCount` | `10` |
| `cms`, `ecommerce` | `Shopify` |
| `payments` | `Stripe` |
| `analytics` | `Google Analytics` |
| `marketingAutomation`, `crm` | `HubSpot` |
| `hosting`, `cdn`, `webServers` | `Cloudflare, jsDelivr` |
| `jsFrameworks`, `programmingLanguages` | `React, Next.js` |
| `technologies` | full list with name, categories and vendor website |
| `matchedTechnologies` | set when you use the `onlyDomainsUsing` lead filter |

## BuiltWith vs Wappalyzer vs this

| | BuiltWith | Wappalyzer | This |
|---|---|---|---|
| Price | from $295/month (API on higher plans) | Pro $250/month | pay per website, no subscription |
| Bulk lists | yes | yes | yes |
| Lead filter by technology | yes | yes | yes (`onlyDomainsUsing`) |
| Works from n8n / Make / Zapier / AI agents | via API | via API | yes, plus Apify MCP server |

Prices as listed on the vendors' pricing pages in September 2026.

## Use cases

- **Sales prospecting** — find companies using a competitor's product or the platform you integrate with
- **Technographics enrichment** — add tech stack columns to a lead list or CRM export
- **Competitor research** — analytics, A/B testing, payments and marketing tools competitors use
- **Agencies** — qualify prospects by CMS (WordPress, Webflow, Shopify…)
- **IT & security audits** — web servers, CDNs and frameworks across many domains

## FAQ

**How is this different from the Wappalyzer / BuiltWith browser extension?** Extensions check one site at a time. This processes whole lists and returns structured data you can filter and export.

**Can it find every website using a technology?** It analyzes the domains you give it. Pair it with any domain source (lead list, Google Maps or search results) and use `onlyDomainsUsing` to keep the matches.

**Is it legal?** It reads publicly available information about websites, not personal data.

*Not affiliated with BuiltWith or Wappalyzer; names are used for comparison only. Examples are MIT licensed.*
