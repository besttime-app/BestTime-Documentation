# Query week

> Query the week (whole forecast):

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/week"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/week?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843'
```

```javascript
const params = new URLSearchParams({ 
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
});

fetch(`https://besttime.app/api/v1/forecasts/week?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

> The above request returns a JSON structured similar as the [new forecast](#new-forecast) endpoint

> Click <a href="https://github.com/besttime-app/slate/blob/master/source/examples/forecast_new/forecast_new_response.json" target="_blank">here</a> for the full JSON response

### Input attributes

The 'query week' endpoint is used to retrieve all data from an existing forecast (every day of the week). The response structure is exactly the same as the [new forecast](#new-forecast) response. Normally API credits are charged for this endpoint, but is free within one day after created a new forecast (through the Venue Search- or directly through the [New Foot Traffic Forecast](#input-attributes-new-forecast) endpoint).

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Week forecast endpoint: https://besttime.app/api/v1/forecasts/week
</aside>

<aside class="notice">
HTTP method: GET
</aside>


### Response attributes

The response attributes are exactly the same as the attributes in the 'new forecast' endpoint.  
 &nbsp;
See [new forecast reponse attributes](#response-attributes-new-forecast)

### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/week`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.