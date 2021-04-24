# Query now raw

> Query the raw hour data for current hour:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/now/raw"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/now/raw?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843'
```

```javascript
const params = new URLSearchParams({ 
  'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
  'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
});

fetch(`https://besttime.app/api/v1/forecasts/now/raw?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes

The 'query now raw' endpoint is used to retrieve the raw data from an existing forecast for one hour of the day. It automatically determines the current day and hour in the local timezone of the venue.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 
- **hour_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the hour (hour of the venue in the local timezone). E.g. `0` means current hour, and `-2` means two hours ago. Range: min `-12`, max `12`. Useful to for example get the forecast for next hour (+1).  
 &nbsp; 

<aside class="notice">
Now raw endpoint: https://besttime.app/api/v1/forecasts/now/raw
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
    "venue_name": "McDonald's",
    "venue_current_gmttime": "Saturday 2020-04-24 04:03AM",
    "venue_current_localtime_iso": "Saturday 2020-04-24 12:02PM"
  }
}
```


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/now/raw`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.

