# Query busy hours

> Query busy hours:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/busy"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_step': 0
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/busy?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&
day_step=0'
```

```javascript
const params = new URLSearchParams({ 
  'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
  'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
  'day_step': 0
});

fetch(`https://besttime.app/api/v1/forecasts/busy?${params}`, {
  method: 'get'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes Query Busy hours

The 'query busy hours' endpoint is used to retrieve all busy hour information from an existing forecast for a specific day of the week.
By default, the response includes the busy hour information for the current day (at the local timezone of the venue). 

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
 - **day_int** `int` <span style="color:blue">OPTIONAL</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday). `day_int` cannot be used in combination with `day_step` and `hour_step`.  
 &nbsp; 
- **day_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the day (day of week of the venue in the local timezone). E.g. `0` means current day, and `1` means tomorrow. Range: min `-31`, max `31`. `day_step` cannot be used in combination with `day_int`.  
 &nbsp;  
- **hour_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the hour (hour of the venue in the local timezone). E.g. `0` means current hour, and `-2` means two hours ago. Range: min `-12`, max `12`. `hour_step` cannot be used in combination with `day_int`.  
 &nbsp;
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Query busy hours endpoint: https://besttime.app/api/v1/forecasts/busy
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON response like this:

```json
{
    "analysis": {
        "busy_hours": [
            {
                "busy_end": 14,
                "busy_end_12": "2PM",
                "busy_end_in": "2 hour and 16 minutes",
                "busy_end_in_sec": 8220,
                "busy_end_passed": 0,
                "busy_period_duration": 4,
                "busy_start": 10,
                "busy_start_12": "10AM",
                "busy_start_in": "Start of busy period already passed",
                "busy_start_in_sec": 0,
                "busy_start_passed": 1
            },
            {
                "busy_end": 20,
                "busy_end_12": "8PM",
                "busy_end_in": "8 hour and 16 minutes",
                "busy_end_in_sec": 29820,
                "busy_end_passed": 0,
                "busy_period_duration": 4,
                "busy_start": 16,
                "busy_start_12": "4PM",
                "busy_start_in": "4 hour and 16 minutes",
                "busy_start_in_sec": 15420,
                "busy_start_passed": 0
            }
        ],
        "busy_hours_list": [
            10,
            11,
            12,
            13,
            16,
            17,
            18,
            19
        ],
        "busy_hours_list_12h": [
            "10AM",
            "11AM",
            "12PM",
            "1PM",
            "4PM",
            "5PM",
            "6PM",
            "7PM"
        ],
        "busy_hours_list_coming": [
            12,
            13,
            16,
            17,
            18,
            19
        ],
        "busy_hours_list_coming_12h": [
            "12PM",
            "1PM",
            "4PM",
            "5PM",
            "6PM",
            "7PM"
        ],
        "day_info": {
            "day_int": 4,
            "day_rank_max": 7,
            "day_rank_mean": 3,
            "day_text": "Friday",
            "venue_open_close_v2": {
                "24h": [
                    {
                        "opens": 6,
                        "opens_minutes": 0,
                        "closes": 23,
                        "closes_minutes": 0,
                        "open_24h": false,
                        "crosses_midnight": false,
                        "day_text": "Friday"
                    }
                ],
                "12h": [
                    "6am–11pm"
                ],
                "special_day": null
            },
            "venue_closed": 23,
            "venue_open": 6
        }
    },
    "epoch_analysis": 1583911633,
    "forecast_updated_on": "2020-03-11T07:27:13.849228+00:00",
    "status": "OK",
    "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
    "venue_info": {
        "venue_current_gmttime": "Fri, 13 Mar 2020 18:43:30 GMT",
        "venue_current_localtime_iso": "2020-03-13T11:43:30.101057-07:00",
        "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles"
    },
    "venue_name": "McDonald's"
}
```

### Response attributes Query Busy hours

- **analysis** `object`  
 Containing the all the busy hour analysis and venue day info.
 - analysis.**busy_hours** `list`  
   List with busy hour objects, containing details of one or multiple busy periods per day.  
  &nbsp;
     - analysis.busy_hours.**busy_start** `int`  
       Start hour of the busy hour, using the 24 hour notation.  
       &nbsp;
     - analysis.busy_hours.**busy_start_passed** `int`  
       Indicates if the busy hour start is already passed. Indicates `1` for passed, `0` for not passed.
       &nbsp;
     - analysis.busy_hours.**busy_start_12** `string`  
       Start hour of the busy hour, using the 12 hour notation.  
       &nbsp;
     - analysis.busy_hours.**busy_start_in** `string`  
       Time remaining until the busy hour starts. Notation 'HH hour and MM minutes'. If busy hour start has been passed it will indicate `Start of busy period already passed`  
       &nbsp;
     - analysis.busy_hours.**busy_start_in_sec** `int`  
       Time remaining until the busy hour starts, in seconds.  
       &nbsp;
     - analysis.busy_hours.**busy_period_duration** `int`  
       Duration of the busy period, in hours.  
       &nbsp;
     - analysis.busy_hours.**busy_end** `int`  
       End hour of the busy hour, using the 24 hour notation.  
       &nbsp;
     - analysis.busy_hours.**busy_end_passed** `int`  
       Indicates if the busy hour end is already passed. Indicates `1` for passed, `0` for not passed.
       &nbsp;
     - analysis.busy_hours.**busy_end_12** `string`  
       End hour of the busy hour, using the 12 hour notation.  
       &nbsp;
     - analysis.busy_hours.**busy_end_in** `string`  
       Time remaining until the busy hour ends. Notation 'HH hour and MM minutes'. If busy hour end has been passed it will indicate `End of busy period already passed`  
       &nbsp;
     - analysis.busy_hours.**busy_end_in_sec** `int`  
       Time remaining until the busy hour ends, in seconds.  
       &nbsp;
 - analysis.**busy_hours_list** `list`  
   List with busy hours (`int`), in 24-hour notation.  
  &nbsp;
 - analysis.**busy_hours_list_12h** `list`  
   List with busy hours (`string`), in 12-hour notation.  
  &nbsp;
 - analysis.**busy_hours_list_coming** `list`  
   List with busy hours (`int`) which still have to come. In 24-hour notation.  
  &nbsp;
 - analysis.**busy_hours_list_coming_12h** `list`  
   List with busy hours (`string`) which still have to come, in 12-hour notation.  
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
     - analysis.day_info.**venue_open_close_v2** `object`
       Object with open and close times for the venue. The object contains two lists: `24h` and `12h`. The `24h` list contains open and close times for the venue in 24 hour notation. The `12h` list contains open and close times for the venue in 12 hour notation. A venue can have multiple opening times per day. Note: requires refreshing the foot traffic forecast if the foot traffic forecast is outdated.
        &nbsp;
        - analysis.day_info.venue_open_close_v2.**24h** `list`
          List with objects describing each opening period in 24 hour notation. Every object contains `opens`, `opens_minutes`, `closes`, `closes_minutes`, `open_24h`, `crosses_midnight`, and `day_text`.
          &nbsp;
        - analysis.day_info.venue_open_close_v2.**12h** `list`
          List with open and close times for the venue in 12 hour notation (matching the `label` values shown in the `24h` objects).
          &nbsp;
        - analysis.day_info.venue_open_close_v2.**special_day** `object|null`
          Optional object describing holiday/special-day overrides. Either `null` or an object with `message` and `name` fields when Google marks a day as special.
          &nbsp;
     - analysis.day_info.**venue_closed** `int`/`string` <span style="color:red">DEPRECATED</span>
       Hour of day when the venue closes. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day. Deprecated, use `venue_open_close_v2` instead.
       &nbsp;
     - analysis.day_info.**venue_open** `int`/`string` <span style="color:red">DEPRECATED</span>
       Hour of day when the venue opens. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day. Deprecated, use `venue_open_close_v2` instead.
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
 - venue_info.**venue_current_gmtttime** `string`  
   Time at the venue in Greenwich Mean Time. Adjusting the `hour_step` and `day_step` will also alter this time.  
 - venue_info.**venue_current_localtime_iso** `string`  
   Local time at the venue. Adjusting the `hour_step` and `day_step` will also alter this time.  
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
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/busy`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.

