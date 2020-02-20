
# API Reference

Introduction text

## Authentication 

There are two types of API keys. Private keys to create a new forecast, and public keys to query data from existing forecasted businesses. The private key can be used to create, delete and list forecasts. As the name suggests, the private key should be kept secret, in order to avoid other people from forecasting new businesses and abusing your limited forecast credits. The public key can be used to query existing business forecasts. It can only used get existing forecast data (read-only). 

API keys are generated in pairs, and you can generate multiple API key sets (pairs) in the API key management page. When using multiple API keys, you should remember that you can only query forecasts from the same key set. 

All key sets use credits from the same account. When an API key is compromised you can delete the API key set through the API Key management page.

<code>api_key_private</code>
<code>api_key_public</code>


## Credits

There are two types of credits. Forecast credits and query credits. 
When forecasting a business using the private API key a 'forecast credit' is substracted from your account. When querying an existing forecast a 'query credit' is substracted from your account. 

Forecast credits are substracted when a forecast is succesfully made and saved on the server. It won't substract a forecast query when:

* The business is not found
* The business is found but it could not be forecasted (when there is not enough data)
* The forecast fails (internal error)

When querying an existing forecast a query credit is subtracted for every request. Each subscription plans contains at least 1000x more query credits than forecast queries. The public API key can only perform read-only actions, but you could choose to hide the public key on public websites (e.g. in your website back-end) to lower your query credit usage (or to prevent abuse).

### Subscription plans
Credits will be added at the start of every monthly invoice cycle, when you upgrade, or when you buy extra credit bundles (only for selected subscription plans). Credits don't expire and automatically roll over to the next month.