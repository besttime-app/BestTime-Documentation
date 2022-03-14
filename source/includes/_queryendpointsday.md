# Query day 

> Query one day of the week:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/day"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_int': 3
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/day?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&
day_int=3'
```

```javascript
const params = new URLSearchParams({ 
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_int': 3
});

fetch(`https://besttime.app/api/v1/forecasts/day?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes Query Day

The 'query day' endpoint is used to retrieve all analysis from an existing forecast for a specific day of the week.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **day_int** `int` <span style="color:blue">OPTIONAL</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday). If not specified, the current day (in local time of the venue) of the week is used.  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Query day endpoint: https://besttime.app/api/v1/forecasts/day
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON response like this:

```json
  {
  "analysis": {
    "busy_hours": [
      9,
      10,
      11
    ],
    "day_info": {
      "day_int": 0,
      "day_rank_max": 6,
      "day_rank_mean": 4,
      "day_text": "Monday",
      "venue_closed": 4,
      "venue_open": 4
    },
    "hour_analysis": [{
        "hour": 6,
        "intensity_nr": -1,
        "intensity_txt": "Below average"
      },
      {
        "hour": 7,
        "intensity_nr": -1,
        "intensity_txt": "Below average"
      },
      {
        "hour": 8,
        "intensity_nr": 0,
        "intensity_txt": "Average"
      },
      ....Other hours hidden. See below for the full JSON response example...
      {
        "hour": 5,
        "intensity_nr": -1,
        "intensity_txt": "Below average"
      }
    ],
    "peak_hours": [{
      "peak_delta_mean_week": 29,
      "peak_end": 23,
      "peak_intensity": 4,
      "peak_max": 11,
      "peak_start": 8
    }],
    "quiet_hours": [
      2,
      3,
      4,
      5
    ],
    "surge_hours": {
      "most_people_come": 8,
      "most_people_leave": 0
    }
  },
  "day_int": 0,
  "epoch_analysis": 1583400856,
  "forecast_updated_on": "2020-03-05T09:34:16.836061+00:00",
  "status": "OK",
  "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
  "venue_name": "McDonald's"
}
```

> Click <a href="https://github.com/besttime-app/slate/blob/master/source/examples/query_day/query_day_response.json" target="_blank">here</a> for the full JSON response


### Response attributes Query Day

- **analysis** `object`  
 Containing the all the included analytics like 'peak_hours', 'busy_hours', etc for the given day. 
 - analysis.**busy_hours** `list`  
   List with busy hours of the day. The hours are in 24 hour `int` notation.  
  &nbsp;
 - analysis.**day_info** `object`  
   Details about the day    
  &nbsp;
     - analysis.day_info.**day_int** `int`  
       Day integer range `0` (Monday) to `6` (Sunday)  
       &nbsp;
     - analysis.day_info.**day_rank_max** `int`  
       Day ranking based on the maximum busyness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most busy day of the week.  
       &nbsp;
     - analysis.day_info.**day_rank_mean** `int`  
       Day ranking based on mean busyness (total volume) of the day. Range `1` to `7`. E.g. `7` indicates the least busy day of the week.  
       &nbsp;
     - analysis.day_info.**day_text** `string`  
       Day name. E.g. `monday`  
       &nbsp;
     - analysis.day_info.**venue_closed** `int`  
       Hour of day when the venue closes. Range `0` to `23` hour  
       &nbsp;
     - analysis.day_info.**venue_open** `int`  
       Hour of day when the venue opens. Range `0` to `23` hour  
       &nbsp;
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
 - analysis.**peak_hours** `list`  
   List with peak objects, containing details of one or multiple peaks per day.  
  &nbsp;
     - analysis.peak_hours.**peak_start** `int`  
       Start hour of the peak, using the 24 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_max** `int`  
       Hour of the day when the peak is at its maximum. Using the 24 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_end** `int`  
       End hour of the peak, using the 24 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_intensity** `int`  
       Intensity of the peak, rated from `1` (minimum) to `5` (maximum)  
       &nbsp;
     - analysis.peak_hours.**peak_delta_mean_week** `int`  
       Percentage how much the peak maximum is above the mean busyness of the week.  
       &nbsp;
 - analysis.**quiet_hours** `list`  
   List with quiet hours of the day. The hours are in 24 hour `int` notation.  
  &nbsp;
 - analysis.**surge_hours** `object`  
   Details at which hour most people enter (come) or leave the venue.
  &nbsp;
     - analysis.surge_hours.**most_people_come** `int`  
       Hour when most people come to the venue during the day window. The hours are in 24 hour `int` notation.  
       &nbsp;
     - analysis.surge_hours.**most_people_leave** `int`  
       Hour when most people leave to the venue during the day window. The hours are in 24 hour `int` notation.  
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
  - venue_info.**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup. Note this name could be slightly different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_address** `string`  
   Address of the venue. This is the address of the venue as found by the geocoding lookup. Note this address could be different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is the primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.
  &nbsp;
 - venue_info.**venue_timezone** `string`  
   The timezone of the venue. E.g. `America/Los Angeles`  
  &nbsp;


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/day`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.

