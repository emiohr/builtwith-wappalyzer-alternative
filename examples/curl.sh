# Tech stack lookup with plain HTTP — one call, JSON back
curl -X POST "https://api.apify.com/v2/acts/jesting_grass~tech-stack-detector/run-sync-get-dataset-items?token=$APIFY_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"domains":["stripe.com","allbirds.com"]}'
