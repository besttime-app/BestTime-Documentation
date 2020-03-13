## Query peak hours

> Query peaks:

```python
import requests
import json

url = "https://BestTime.app/api/v1/query/peaks/"

headers = {
    'Content-Type': 'application/json'
}

payload = json.dumps({
  "api_key_public": "352a9addc0ac4c599572e56f504080d3",
	"venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
  "hour_step":1,
  "day_step":0
})

response = requests.request("POST", url, headers=headers, data = payload)

response_dict = json.loads(response.text.encode('utf8'))
```

```shell
# cURL
curl --location --request POST 'https://BestTime.app/api/v1/query/peaks/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key_public": "352a9addc0ac4c599572e56f504080d3",
	"venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
  "hour_step":1,
  "day_step":0
}	'
```

```javascript
var settings = {
  "url": "https://BestTime.app/api/v1/query/peaks/",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    	"api_key_public": "352a9addc0ac4c599572e56f504080d3",
	    "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
      "hour_step":1,
      "day_step":0
    }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

### Input attributes Query Peaks

The 'query peaks' endpoint is used to retrieve all peaks from an existing forecast for a specific day of the week.
By default, the response includes the peak objects for the current day (at the local timezone of the venue) `peak_hours`. Additionally, it contains a list with peak objects `peaks_coming` which only contains the peaks from `peak_hours` which have not passed yet.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **hour_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the hour (hour of the venue in the local timezone). E.g. `0` means current hour, and `-2` means two hours ago. Range: min `-12`, max `12`.  
 &nbsp; 
- **day_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the day (day of week of the venue in the local timezone). E.g. `0` means current day, and `1` means tomorrow. Range: min `-31`, max `31`.  
 &nbsp;  
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-keys)  
 &nbsp; 

<aside class="notice">
Query peak endpoint: https://BestTime.app/api/v1/query/peaks/
</aside>

<aside class="notice">
HTTP method: POST
</aside>


> The above request returns a JSON response like this:

```json
{
    "analysis": {
        "day_info": {
            "day_int": 1,
            "day_rank_max": 2,
            "day_rank_mean": 4,
            "day_text": "Tuesday",
            "venue_closed": 4,
            "venue_open": 4
        },
        "peak_hours": [
            {
                "peak_delta_mean_week": 37,
                "peak_end": 18,
                "peak_end_12h": "6PM",
                "peak_end_in": "2 hour and 40 minutes",
                "peak_end_in_sec": 9660,
                "peak_end_passed": 0,
                "peak_intensity": 5,
                "peak_max": 13,
                "peak_max_12h": "1PM",
                "peak_max_in": "Peak maximum already passed",
                "peak_max_in_sec": 0,
                "peak_max_passed": 1,
                "peak_start": 7,
                "peak_start_12h": "7AM",
                "peak_start_in": "Peak already started",
                "peak_start_passed": 1
            },
            {
                "peak_delta_mean_week": 12,
                "peak_end": 23,
                "peak_end_12h": "11PM",
                "peak_end_in": "7 hour and 41 minutes",
                "peak_end_in_sec": 27660,
                "peak_end_passed": 0,
                "peak_intensity": 3,
                "peak_max": 21,
                "peak_max_12h": "9PM",
                "peak_max_in": "5 hour and 41 minutes",
                "peak_max_in_sec": 20460,
                "peak_max_passed": 0,
                "peak_start": 18,
                "peak_start_12h": "6PM",
                "peak_start_in": "2 hour and 40 minutes",
                "peak_start_in_sec": 9660,
                "peak_start_passed": 0
            }
        ]
    },
    "epoch_analysis": 1583400856,
    "forecast_updated_on": "2020-03-05T09:34:16.842016+00:00",
    "status": "OK",
    "venue_info": {
        "venue_current_gmttime": "Tue, 10 Mar 2020 22:19:56 GMT",
        "venue_current_localtime_iso": "2020-03-10T15:19:56.979659-07:00",
        "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles"
    }
}
```

### Response attributes Query Peaks


- **analysis** `object`  
 Containing the all the peak analysis and venue day info.
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
 - analysis.**peak_hours** `list`  
   List with peak objects, containing details of one or multiple peaks per day.  
  &nbsp;
     - analysis.peak_hours.**peak_start** `int`  
       Start hour of the peak, using the 24 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_start_passed** `int`  
       Indicates if the peak start is already passed. Indicates `1` for passed, `0` for not passed.
       &nbsp;
     - analysis.peak_hours.**peak_start_12** `string`  
       Start hour of the peak, using the 12 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_start_in** `string`  
       Time remaining until the peak starts. Notation 'HH hour and MM minutes'. If peak start has been passed it will indicate `Peak start already passed`  
       &nbsp;
     - analysis.peak_hours.**peak_start_in_sec** `int`  
       Time remaining until the peak starts, in seconds.  
       &nbsp;
     - analysis.peak_hours.**peak_max** `int`  
       Hour of the day when the peak is at its maximum. Using the 24 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_max_passed** `int`  
       Indicates if the peak max is already passed. Indicates `1` for passed, `0` for not passed.  
       &nbsp;
     - analysis.peak_hours.**peak_max_12** `string`  
       Hour of the day when the peak is at its maximum. Using the 12 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_max_in** `string`  
       Time remaining until the peak is at its maximum. Notation 'HH hour and MM minutes'. If peak start has been passed it will indicate `Peak maximum already passed`  
       &nbsp;
     - analysis.peak_hours.**peak_max_in_sec** `int`  
       Time remaining until the peak is at its maximum, in seconds
       &nbsp;
     - analysis.peak_hours.**peak_end** `int`  
       End hour of the peak, using the 24 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_end_passed** `int`  
       Indicates if the peak end is already passed. Indicates `1` for passed, `0` for not passed.  
       &nbsp;
     - analysis.peak_hours.**peak_end_12** `string`  
       End hour of the peak, using the 12 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_end_in** `string`  
       Time remaining until the peak ends. Notation 'HH hour and MM minutes'. If peak start has been passed it will indicate `Peak end already passed`  
       &nbsp;
     - analysis.peak_hours.**peak_end_in_sec** `int`  
       Time remaining until the peak ends, in seconds.  
       &nbsp;
     - analysis.peak_hours.**peak_intensity** `int`  
       Intensity of the peak, rated from `1` (minimum) to `5` (maximum)  
       &nbsp;
     - analysis.peak_hours.**peak_delta_mean_week** `int`  
       Percentage how much the peak maximum is above the mean busyness of the week.  
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
