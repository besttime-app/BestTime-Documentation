
# Query hour 

> Query a specific hour of the week:

```python
import requests
import json

url = "https://besttime.app/api/v1/forecasts/hour"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_int': 3,
    'hour':23
}

response = requests.request("GET", url, params=params)

data = json.loads(response.text)

print(data)
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/hour?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&
day_int=3&
hour=23'
```

```javascript
var params = {
      'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
      'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
      'day_int': 3,
      'hour': 23
}

$.ajax({
"url": "https://besttime.app/api/v1/forecasts/hour?" + new URLSearchParams(params),
"method": "GET"
}).done(function (response) {
    console.log(response);
});
```

### Input attributes Query Hour

The 'query hour' endpoint is used to retrieve the 'hour analysis' forecast for the given hour and day of the week.  

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
Hour forecast endpoint: https://besttime.app/api/v1/forecasts/hour
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON reponse like this:

```json
{
    "analysis": {
        "hour_analysis": {
            "hour": 23,
            "intensity_nr": 0,
            "intensity_txt": "Average"
        }
    },
    "day_int": 3,
    "epoch_analysis": 1583400856,
    "forecast_updated_on": "2020-03-05T09:34:16.842662+00:00",
    "status": "OK",
    "venue_info": {
        "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
        "venue_name": "McDonald's"
    }
}
```

> Click <a href="https://github.com/besttime-app/slate/blob/master/source/examples/query_hour/query_hour_response.json" target="_blank">here</a> for the raw JSON response.

### Response attributes Query Hour
- **analysis** `object`  
 Containing the all the included analytics like 'peak_hours', 'busy_hours', etc for the given day. 
 - analysis.**hour_analysis** `list`  
   List with hour objects, containing details per hour.  
   &nbsp;
    - analysis.hour_analysis.**hour** `int`  
      Hour integer range `0` (midnight) to `23` (11pm). Please note that the hour window within a weekday starts at 6AM `hour = 6` and ends at 5AM `hour = 5`. See Introduction section [Forecast day window and weekdays](#forecast-day-window-and-weekdays)  
      &nbsp;
    - analysis.hour_analysis.**intensity_nr** `int`  
      Hour intensity_nr indicates how busy the venue is on a scale of 5, ranging from `-2` to `2`. When the venue is closed at the given hour it indicates `999`. See `intensity_txt` for the textual version of the same scale.  
      &nbsp;
    - analysis.hour_analysis.**intensity_txt** `string`  
      Hour intensity_txt indicates how busy the venue is on a scale of 5. See `intensity_nr` for the integer version of the same scale. The intensity is either `Low`, `Below average`, `Average`, `Above average`, or `High`. When the venue is closed at the given hour it indicates `Closed`.  
      &nbsp;
- **day_int** `int`  
  Day integer range `0` (Monday) to `6` (Sunday)  
  &nbsp;
- **epoch_analysis** `int`  
 Epoch timestamp when the forecast was made.  
 &nbsp; 
- **forecast_updated_on** `TimeZone Aware DateTime string`  
 Date and time (Time Zone aware) of the original forecast.  
 &nbsp; 
- **status** `string`  
 Status of the response. Either `OK` or `Error`.  
 &nbsp;
- **venue_info** `object`  
 Details of the forecasted venue.  
 &nbsp; 
 - venue_info.**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding  result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.  
  &nbsp;
 - venue_info.**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup. Note this name could be slightly different than the `venue_address` used as input.  
  &nbsp;


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/hour`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.

