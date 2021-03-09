# Venue collections TODO

> Group venues together in collections:

```python
import requests
import json

url = "https://besttime.app/api/v1/venues/search"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
}

response = requests.request("GET", url, params=params)

data = json.loads(response.text)

print(data)
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/venues/search?api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&q=quiet%20supermarkets%20in%20sydney%20australia%20sunday%20morning&num=100&fast=false&opened=now'


```

```javascript
var params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
}

$.ajax({
"url": "https://besttime.app/api/v1/forecasts/week/raw?" + new URLSearchParams(params),
"method": "GET"
}).done(function (response) {
    console.log(response);
});
```

### Input attributes

The 'query week raw' endpoint is used to retrieve the raw data from an existing forecast (every day of the week).

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-keys)  
 &nbsp; 

<aside class="notice">
Week raw endpoint: https://BestTime.app/api/v1/forecasts/week/raw
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns JSON structured like this:

```json
{
    "analysis": {
        "week_raw": [
            0.0,
            10.0,
            30.0,
            60.0,
            80.0,
            90.0,
            100.0,
            Other hours hidden 
            50.0,
            40.0,
            40.0,
            30.0,
            10.0,
            0.0,
            0.0
        ]
    },
    "epoch_analysis": 1585875838,
    "forecast_updated_on": "2020-04-03T01:03:58.692417+00:00",
    "venue_name": "McDonald's"
}
```

### Alternative split per day data
Using the endpoint `https://besttime.app/api/v1/forecasts/week/raw2` will result in the same response but split per day using the day window from 6am till 5am next day.

```json
{
    "analysis": {
        "week_raw": [
            {
                "day_int": 0,
                "day_raw": [
                    20,
                    30,
                    40,
                    50,
                    60,
                    ...
                    60,
                    50,
                    40,
                    30,
                    20,
                    0,
                    20,
                    20
                ]
            },
            ....
        ]
    },
    "status": "OK",
    "window": {
        "day_window_end_int": 6,
        "day_window_end_txt": "Monday",
        "day_window_start_int": 0,
        "day_window_start_txt": "Monday",
        "time_window_end": 5,
        "time_window_end_12h": "5AM",
        "time_window_start": 6,
        "time_window_start_12h": "6AM",
        "week_window": "Monday 6AM until Monday 5AM next week"
    }
}
```


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/week/raw`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.

