# Query hour raw

> Query the raw hour data:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/hour/raw"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_int': 3,
    'hour': 16
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/hour/raw?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&day_int=3&hour=16'
```

```javascript
const params = new URLSearchParams({ 
  'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
  'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
  'day_int':3,
  'hour':16
});

fetch(`https://besttime.app/api/v1/forecasts/hour/raw?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes

The 'query hour raw' endpoint is used to retrieve the raw data from an existing forecast for one hour of the day.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **day_int** `int` <span style="color:orange">REQUIRED</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday).  
 &nbsp;
- **hour** `int` <span style="color:orange">REQUIRED</span>  
 Hour of the day. Range `0` (Midnight) to `23` (11pm). Please note that the day window within a weekday starts at 6AM `hour = 6` and ends at 5AM `hour = 5` next day. See Introduction section [Forecast day window and weekdays](#forecast-day-window-and-weekdays)  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Hour raw endpoint: https://besttime.app/api/v1/forecasts/hour/raw
</aside>

<aside class="notice">
HTTP method: GET
</aside>

> The above request returns JSON structured like this:

```json
{
  "analysis": {
    "hour_analysis": {
      "hour": 16,
      "intensity_nr": 0,
      "intensity_txt": "Average"
    },
    "hour_raw": 70
  },
  "epoch_analysis": 1585890444,
  "forecast_updated_on": "2020-04-03T05:07:26.012357+00:00",
  "status": "OK",
  "venue_info": {
    "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
    "venue_name": "McDonald's"
  }
}
```


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/hour/raw`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.

