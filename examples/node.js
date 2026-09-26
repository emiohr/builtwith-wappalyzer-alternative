// Website tech stack lookup in Node.js — npm i apify-client
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('jesting_grass/tech-stack-detector').call({
    domains: ['stripe.com', 'allbirds.com', 'hubspot.com'],
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const row of items) console.log(row.domain, '|', row.cms, '|', row.technologyNames);
