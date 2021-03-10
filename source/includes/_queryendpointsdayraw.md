## Query day raw

> Query the raw day data:

```python
import requests
import json

url = "https://beta.besttime.app/api/v1/forecasts/day/raw"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_int': 3
}

response = requests.request("GET", url, params=params)

data = json.loads(response.text)

print(data)
```

```shell
# cURL
curl --location --request GET 'https://beta.besttime.app/api/v1/forecasts/day/raw?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&
day_int=3'
```

```javascript
var params = {
   'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_int': 3
}

$.ajax({
"url": "https://beta.besttime.app/api/v1/forecasts/day/raw?" + new URLSearchParams(params),
"method": "GET"
}).done(function (response) {
    console.log(response);
});
```

### Input attributes

The 'query day raw' endpoint is used to retrieve the raw data from an existing forecast for one day of the week.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **day_int** `int` <span style="color:orange">REQUIRED</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday).  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-keys)  
 &nbsp; 

<aside class="notice">
Day raw endpoint: https://beta.besttime.app/api/v1/forecasts/day/raw
</aside>

<aside class="notice">
HTTP method: GET
</aside>

> The above request returns JSON structured like this:

```json
{
    "analysis": {
        "day_raw": [
            0.0,
            40.0,
            60.0,
            70.0,
            80.0,
            90.0,
            90.0,
            90.0,
            90.0,
            80.0,
            70.0,
            70.0,
            70.0,
            70.0,
            70.0,
            70.0,
            60.0,
            50.0,
            40.0,
            30.0,
            20.0,
            10.0,
            0.0,
            0.0
        ]
    },
    "epoch_analysis": 1585875838,
    "forecast_updated_on": "2020-04-03T01:03:58.685394+00:00",
    "status": "OK"
}
```


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://beta.besttime.app/api/v1/forecasts/day/raw`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.

