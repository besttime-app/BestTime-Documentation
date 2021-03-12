# Query weekoverview

> Query the week overview:

```python
import requests
import json

url = "https://beta.besttime.app/api/v1/forecasts/weekoverview"

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
curl --location --request GET 'https://beta.besttime.app/api/v1/forecasts/weekoverview?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843'
```

```javascript
var params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
}

$.ajax({
"url": "https://beta.besttime.app/api/v1/forecasts/weekoverview?" + new URLSearchParams(params),
"method": "GET"
}).done(function (response) {
    console.log(response);
});
```


### Input attributes

The 'query week' endpoint is used to retrieve all data from an existing forecast (every day of the week). The response structure is exactly the same as the [new forecast](#new-forecast) response. 

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Week overview endpoint: https://beta.besttime.app/api/v1/forecasts/weekoverview
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON response like this:

```json
{
    "analysis": {
        "week_overview": [
            {
                "day_int": 0,
                "day_max": 100,
                "day_mean": 57,
                "day_rank_max": 1,
                "day_rank_mean": 6,
                "day_text": "Monday",
                "venue_closed": 4,
                "venue_open": 4
            },
            {
                "day_int": 1,
                "day_max": 96,
                "day_mean": 58,
                "day_rank_max": 3,
                "day_rank_mean": 5,
                "day_text": "Tuesday",
                "venue_closed": 4,
                "venue_open": 4
            },
            {
                "day_int": 2,
                "day_max": 99,
                "day_mean": 62,
                "day_rank_max": 2,
                "day_rank_mean": 1,
                "day_text": "Wednesday",
                "venue_closed": 4,
                "venue_open": 4
            },
            {
                "day_int": 3,
                "day_max": 87,
                "day_mean": 59,
                "day_rank_max": 6,
                "day_rank_mean": 4,
                "day_text": "Thursday",
                "venue_closed": 4,
                "venue_open": 4
            },
            {
                "day_int": 4,
                "day_max": 88,
                "day_mean": 61,
                "day_rank_max": 5,
                "day_rank_mean": 2,
                "day_text": "Friday",
                "venue_closed": 4,
                "venue_open": 4
            },
            {
                "day_int": 5,
                "day_max": 85,
                "day_mean": 60,
                "day_rank_max": 7,
                "day_rank_mean": 3,
                "day_text": "Saturday",
                "venue_closed": 4,
                "venue_open": 4
            },
            {
                "day_int": 6,
                "day_max": 93,
                "day_mean": 54,
                "day_rank_max": 4,
                "day_rank_mean": 7,
                "day_text": "Sunday",
                "venue_closed": 4,
                "venue_open": 4
            }
        ]
    },
    "forecast_updated_on": "2020-04-03T01:03:58.692417+00:00",
    "status": "OK"
}
```

### Response attributes Weekoverview


- **analysis** `object`  
 Containing the analysis.
 - analysis.**week_overview** `list`  
   List with day objects, containing overview details per day.  
  &nbsp;
       - analysis.weekoverview[day].**day_int** `int`  
       Day integer range `0` (Monday) to `6` (Sunday)  
       &nbsp;
       - analysis.weekoverview[day].**day_max** `int`  
       Indicating the maximum busyness percentage. Values (0 - 100%) are based on the hour with the most visitors of the day, relative to the biggest peak of the week for this venue.
       &nbsp;
       - analysis.weekoverview[day].**day_mean** `int`  
       Indicating the average busyness percentage (0 - 100%). Values are based on the total visitors (volume) of the day, relative to the biggest peak of the week for this venue. 
       &nbsp;
     - analysis.weekoverview[day].**day_rank_max** `int`  
       Day ranking based on the maximum busyness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most busy day of the week.  
       &nbsp;
     - analysis.weekoverview[day].**day_rank_mean** `int`  
       Day ranking based on mean busyness (total volume) of the day. Range `1` to `7`. E.g. `7` indicates the least busy day of the week.  
       &nbsp;
     - analysis.weekoverview[day].**day_text** `string`  
       Day name. E.g. `monday`  
       &nbsp;
     - analysis.weekoverview[day].**venue_closed** `int`  
       Hour of day when the venue closes. Range `0` to `23` hour  
       &nbsp;
     - analysis.weekoverview[day].**venue_open** `int`  
       Hour of day when the venue opens. Range `0` to `23` hour  
       &nbsp;
- **forecast_updated_on** `TimeZone Aware DateTime string`  
 Date and time (Time Zone aware) of the original forecast.  
 &nbsp; 
- **status** `string`  
 Status of the response. Either `OK` or `Error`.  
 &nbsp; 

 ### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://beta.besttime.app/api/v1/forecasts/weekoverview`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.