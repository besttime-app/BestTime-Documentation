## Query quiet hours

> Query quiet hours:

```python
import requests
import json

url = "https://besttime.app/api/v1/forecasts/quiet"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_step': 0,
    'hour_step':0
}

response = requests.request("GET", url, params=params)

data = json.loads(response.text)

print(data)
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/quiet?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&
day_step=0&
hour_step=0'
```

```javascript
var params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_step': 0,
    'hour_step': 0
}

$.ajax({
"url": "https://besttime.app/api/v1/forecasts/quiet?" + new URLSearchParams(params),
"method": "GET"
}).done(function (response) {
    console.log(response);
});
```

### Input attributes Query Quiet hours

The 'query quiet hours' endpoint is used to retrieve all quiet hour information from an existing forecast for a specific day of the week.
By default, the response includes the quiet hour information for the current day (at the local timezone of the venue). 

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
 Public API Key. See more info on [API keys](#api-keys)  
 &nbsp; 

<aside class="notice">
Query quiet hours endpoint: https://BestTime.app/api/v1/forecasts/quiet
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON response like this:

```json
{
    "analysis": {
        "day_info": {
            "day_int": 4,
            "day_rank_max": 7,
            "day_rank_mean": 3,
            "day_text": "Friday",
            "venue_closed": 4,
            "venue_open": 4
        },
        "quiet_hours": [
            {
                "quiet_end": 8,
                "quiet_end_12": "8AM",
                "quiet_end_in": "End of quiet period already passed",
                "quiet_end_in_sec": 0,
                "quiet_end_passed": 1,
                "quiet_period_duration": 2,
                "quiet_start": 6,
                "quiet_start_12": "6AM",
                "quiet_start_in": "Start of quiet period already passed",
                "quiet_start_in_sec": 0,
                "quiet_start_passed": 1
            },
            {
                "quiet_end": 6,
                "quiet_end_12": "6AM",
                "quiet_end_in": "18 hour and 7 minutes",
                "quiet_end_in_sec": 65280,
                "quiet_end_passed": 0,
                "quiet_period_duration": 3,
                "quiet_start": 3,
                "quiet_start_12": "3AM",
                "quiet_start_in": "15 hour and 7 minutes",
                "quiet_start_in_sec": 54480,
                "quiet_start_passed": 0
            }
        ],
        "quiet_hours_list": [
            6,
            7,
            3,
            4,
            5
        ],
        "quiet_hours_list_12h": [
            "6AM",
            "7AM",
            "3AM",
            "4AM",
            "5AM"
        ],
        "quiet_hours_list_coming": [
            3,
            4,
            5
        ],
        "quiet_hours_list_coming_12h": [
            "3AM",
            "4AM",
            "5AM"
        ]
    },
    "epoch_analysis": 1583911633,
    "forecast_updated_on": "2020-03-11T07:27:13.849228+00:00",
    "status": "OK",
    "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
    "venue_info": {
        "venue_current_gmttime": "Fri, 13 Mar 2020 18:52:28 GMT",
        "venue_current_localtime_iso": "2020-03-13T11:52:28.890102-07:00",
        "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles"
    },
    "venue_name": "McDonald's"
}
```

### Response attributes Query Quiet hours


- **analysis** `object`  
 Containing the all the quiet hour analysis and venue day info.
 - analysis.**quiet_hours** `list`  
   List with quiet hour objects, containing details of one or multiple quiet periods per day.  
  &nbsp;
     - analysis.quiet_hours.**quiet_start** `int`  
       Start hour of the quiet hour, using the 24 hour notation.  
       &nbsp;
     - analysis.quiet_hours.**quiet_start_passed** `int`  
       Indicates if the quiet hour start is already passed. Indicates `1` for passed, `0` for not passed.
       &nbsp;
     - analysis.quiet_hours.**quiet_start_12** `string`  
       Start hour of the quiet hour, using the 12 hour notation.  
       &nbsp;
     - analysis.quiet_hours.**quiet_start_in** `string`  
       Time remaining until the quiet hour starts. Notation 'HH hour and MM minutes'. If quiet hour start has been passed it will indicate `Start of quiet period already passed`  
       &nbsp;
     - analysis.quiet_hours.**quiet_start_in_sec** `int`  
       Time remaining until the quiet hour starts, in seconds.  
       &nbsp;
     - analysis.quiet_hours.**quiet_period_duration** `int`  
       Duration of the quiet period, in hours.  
       &nbsp;
     - analysis.quiet_hours.**quiet_end** `int`  
       End hour of the quiet hour, using the 24 hour notation.  
       &nbsp;
     - analysis.quiet_hours.**quiet_end_passed** `int`  
       Indicates if the quiet hour end is already passed. Indicates `1` for passed, `0` for not passed.
       &nbsp;
     - analysis.quiet_hours.**quiet_end_12** `string`  
       End hour of the quiet hour, using the 12 hour notation.  
       &nbsp;
     - analysis.quiet_hours.**quiet_end_in** `string`  
       Time remaining until the quiet hour ends. Notation 'HH hour and MM minutes'. If quiet hour end has been passed it will indicate `End of quiet period already passed`  
       &nbsp;
     - analysis.quiet_hours.**quiet_end_in_sec** `int`  
       Time remaining until the quiet hour ends, in seconds.  
       &nbsp;
 - analysis.**quiet_hours_list** `list`  
   List with quiet hours (`int`), in 24-hour notation.  
  &nbsp;
 - analysis.**quiet_hours_list_12h** `list`  
   List with quiet hours (`string`), in 12-hour notation.  
  &nbsp;
 - analysis.**quiet_hours_list_coming** `list`  
   List with quiet hours (`int`) which still have to come. In 24-hour notation.  
  &nbsp;
 - analysis.**quiet_hours_list_coming_12h** `list`  
   List with quiet hours (`string`) which still have to come, in 12-hour notation.  
  &nbsp;
- analysis.**day_info** `object`  
   Details about the day    
  &nbsp;
     - analysis.day_info.**day_int** `int`  
       Day integer range `0` (Monday) to `6` (Sunday)  
       &nbsp;
     - analysis.day_info.**day_rank_max** `int`  
       Day ranking based on the maximum quietness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most quiet day of the week.  
       &nbsp;
     - analysis.day_info.**day_rank_mean** `int`  
       Day ranking based on mean quietness (total volume) of the day. Range `1` to `7`. E.g. `7` indicates the least quiet day of the week.  
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
   Local time at the venue in ISO standard format. Adjusting the `hour_step` and `day_step` will also alter this time.  
  &nbsp;
 - venue_info.**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is the primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.
  &nbsp;
 - venue_info.**venue_timezone** `string`  
   The timezone of the venue. E.g. `America/Los Angeles`  
  &nbsp;
