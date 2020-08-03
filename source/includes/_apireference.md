
# API Reference

The API Reference explains how:

- authentication works using the API Keys.
- credits are handled with your API usage.
- to create a new venue forecast.
- to query an existing forecast to get specific, or more detailed data.

## <a name="api-keys"></a> API Key

BestTime.app uses API keys to allow access to the API. You can find or generate API keys at the [API keys Management](http://besttime.app/api/v1/api_keys_list) page.

BestTime.app expects for the API key to be included in all API requests to the server. 
Our API accepts only JSON-encoded POST requests and returns JSON-encoded responses.
This makes it easier to request venue names and addresses without the need to encode the parameters (like you would usually need to do with GET query parameters).

Authentication for the API is done using API keys.
There are two types of API keys; Private keys are used to create a new forecast, and public keys to query data from existing forecasted venues. The private key can be used to create, delete and list forecasts. As the name suggests, the private key should be kept secret, to avoid other people from forecasting new venues and abusing your limited forecast credits. The public key can be used to query existing venue forecasts. However, it can only be used to get existing forecast data (read-only). 

API keys are generated in pairs, and you can generate multiple API key sets (pairs) in the API key management page. When using multiple API keys, you should remember that you can only query forecasts from the same key set. 

All key set use credits from the same account. When an API key is compromised you can delete the API key set through the API Key management page.

## Authentication

> To authorize, use this code:


```python
import requests

url = "https://besttime.app/api/v1/keys/pri_a00de9e302662c0217a9cf08ab304122"

payload = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/keys/pri_a00de9e302662c0217a9cf08ab304122'
```

```javascript
var settings = {
  "url": "https://besttime.app/api/v1/keys/pri_a00de9e302662c0217a9cf08ab304122",
  "method": "GET"
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

You can find or generate API keys at the [API keys Management](http://besttime.app/api/v1/api_keys_list) page.

> The above command returns JSON structured like this:

```json
  {
    "active": true,
    "api_key_private": "pri_a00de9e302662c0217a9cf08ab304122",
    "api_key_public": "pub_e11661721b084d36b8f469a2c012e754",
    "credits_forecast": 300,
    "credits_query": 10000000,
    "status": "OK",
    "valid": true
  }
```

### Private and public API keys

- **api_key_private** `string`  
 32 Character private API key. Used to create new forecasts or get live data.  
 &nbsp; 
- **api_key_public** `string`  
 32 Character public API key. Used to query (lookup) specific data from an excisting forecast.  
 &nbsp;  

<aside class="notice">
Base endpoint: https://BestTime.app/api/v1/keys
</aside>

<aside class="notice">
HTTP method: GET
</aside>


<aside class="notice">
Make sure to replace <code>pri_a00de9e302662c0217a9cf08ab304122</code> with your 36 char private API key.
</aside>


## Credits

There are two types of credits. Forecast credits and query credits. 
When forecasting a venue using the private API key a 'forecast credit' is subtracted from your account. When querying an existing forecast a 'query credit' is subtracted from your account. 

Forecast credits are subtracted when a forecast is successfully made and saved on the server. It won't subtract a forecast query when:

* The venue is not found
* The venue is found but it could not be forecasted (when there is not enough data)
* The forecast fails (internal error)

When querying an existing forecast a query credit is subtracted for every request. Each subscription plan contains at least 1000x more query credits than forecast queries. The public API key can only perform read-only actions, but you could choose to hide the public key on public websites (e.g. in your website back-end) to lower your query credit usage (or to prevent abuse).

| Goal                               | Credits used     | API Key required | Parameter       |
|------------------------------------|------------------|------------------|-----------------|
| Create a new forecast              | Forecast credits | Private          | api_key_private |
| Get live data (platinum only)     | Forecast credits | Private          | api_key_private |
| List all forecast by venue_id   | None             | Private          | api_key_private |
| Query data from existing forecasts | Query credits    | Public           | api_key_public  |

### Subscription plans
Credits will be added at the start of every monthly invoice cycle, when you upgrade, or when you buy extra credit bundles (only for selected subscription plans). Credits don't expire and automatically roll over to the next month. If you cancel your subscription coins will stay in your account. However, all your API keys will be deactivated. This means you cannot create new forecasts and query existing forecasts. If you decide to re-subscribe on the same account you can use your old coins, but you cannot access the previous forecasts anymore.
