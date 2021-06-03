
# New foot-traffic forecast
<a name="forecast-new-link"></a> 

> Returns foot-traffic forecast for a venue based on a name and address

```python
import requests

url = "https://besttime.app/api/v1/forecasts"

params = {
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
    'venue_name': 'McDonalds',
    'venue_address': 'Ocean Ave, San Fransisco'
}

response = requests.request("POST", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request POST 'https://besttime.app/api/v1/forecasts?
api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&
venue_name=McDonalds&
venue_address=Ocean%20Ave%2C%20San%20Fransisco'
```

```javascript
const params = new URLSearchParams({ 
 'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
  'venue_name': 'McDonalds',
  'venue_address': 'Ocean Ave, San Fransisco'
});

fetch(`https://besttime.app/api/v1/forecasts?${params}`, {
  method: 'POST'
}).then(function(data) { 
  console.log(data); 
});
```

> The above request returns JSON structured like this:

```json
  {
    "analysis": [
        {
            "day_info": {
                "day_int": 0,
                "day_rank_max": 6,
                "day_rank_mean": 4,
                "day_text": "Monday",
                "venue_closed": 6,
                "venue_open": 23
            },
            "day_raw": [
                10,
                25,
                40,
                55,
                65,
                75,
                75,
                75,
                75,
                75,
                70,
                65,
                50,
                40,
                30,
                25,
                25,
                25,
                20,
                15,
                10,
                0,
                5,
                5
            ],
            "hour_analysis": [
                {
                    "hour": 6,
                    "intensity_nr": -1,
                    "intensity_txt": "Below average"
                },
                ... Other hours hidden. See full JSON example link below
            ],
            "peak_hours": [
                {
                    "peak_start": 8,
                    "peak_max": 11,
                    "peak_end": 23,
                    "peak_intensity": 4
                }
            ],
            "quiet_hours": [
                6,
                1,
                2,
                3
            ],
            "busy_hours": [
                9,
                10,
                11,
                12
            ],
            "surge_hours": {
                "most_people_come": 8,
                "most_people_leave": 22
            },
        },
        ... Other days hidden. See full JSON example link below
    ],
    "epoch_analysis": "1583314752",
    "status": "OK",
    "venue_info": {
        "venue_address": "1201 Ocean Ave San Francisco, CA 94112 United States",
        "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles"
    }
}}
```

> Click <a href="https://github.com/besttime-app/slate/blob/master/source/examples/forecast_new/forecast_new_response.json" target="_blank">here</a> for the full JSON response


The 'new forecast' endpoint is used to create a [forecast](#forecasts) of a venue based on the most recent available data. Forecasts are created using the venue name and address as input. The response includes the forecast (including different analysis), and venue information.
The venue information includes the `venue_id`. This ID is the primary parameter to lookup previously forecasted venues, using the [query endpoints] (#query-endpoints). Forecasts are stored on the server for a certain amount of days (see [data retention](#data-retention))

### Input attributes New Forecast

- **venue_name** `string` <span style="color:orange">REQUIRED</span>  
 Name of the venue (public business)  
 &nbsp; 
- **venue_address** `string` <span style="color:orange">REQUIRED</span>  
 Address of the venue (public business). The address does not have to be exact, but needs to be precise enough for the geocoder engine to find the correct venue. The more specific the address the higher chance the geocoder will find the venue. The response object will also display the `venue_name` and `venue_address`, but is using the name and address of the geocoder's found venue. Check the `venue_name` and `venue_address` in the response object to verify if the correct venue has been forecasted.  
 &nbsp; 
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-reference)
 &nbsp; 

<aside class="notice">
New forecast endpoint: https://besttime.app/api/v1/forecasts
</aside>

<aside class="notice">
HTTP method: POST
</aside>

<aside class="warning">
By default the API is limited to 10 requests per second. Contact us for higher limits.
</aside>


### Response attributes New Forecast <a name="responseattributesnewforecast"></a>

- **analysis** `list`  
 List with an analysis object for each day of the week, containing analysis like 'peak_hours', 'busy_hours', etc per day. The list contains days `object` and are sorted on day of the week: `day_int` `0` (Monday) to `6` (Sunday).  
 &nbsp; 
 - analysis[day_int].**busy_hours** `list`  
   List with busy hours of the day. The hours are in 24 hour `int` notation.  
  &nbsp;
 - analysis[day_int].**day_info** `object`  
   Details about the day.   
  &nbsp;
     - analysis[day_int].day_info.**day_int** `int`  
       Day integer range `0` (Monday) to `6` (Sunday)  
       &nbsp;
     - analysis[day_int].day_info.**day_rank_max** `int`  
       Day ranking based on maximum busyness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most busy day of the week.  
       &nbsp;
     - analysis[day_int].day_info.**day_rank_mean** `int`  
       Day ranking based on mean busyness (total volume) of the day. Range `1` to `7`. E.g. `7` indicates the least busy day of the week.  
       &nbsp;
     - analysis[day_int].day_info.**day_text** `string`  
       Day name. E.g. `monday`  
       &nbsp;
     - analysis[day_int].day_info.**venue_closed** `int`  
       Hour of day when the venue closes. Range `0` to `23` hour  
       &nbsp;
     - analysis[day_int].day_info.**venue_open** `int`  
       Hour of day when the venue opens. Range `0` to `23` hour  
       &nbsp;
 - analysis[day_int].**day_raw** `list`  
   List of raw busyness data for each hour of the day, or within the selected hour range. The list contains percentages ranging from `0` to `100`. Indicating the busyness percentage. Percentages are based on historical visits for the given hour, relative to the biggest peak of the week for this venue. When the `now` or `live` parameter is `true` the list will contain one `int` for the current hour in the local time.  
    &nbsp;
 - analysis[day_int].**hour_analysis** `list`  
   List with hour objects, containing details per hour.  
  &nbsp;
     - analysis[day_int].hour_analysis.**hour** `int`  
       Hour integer range `0` (midnight) to `23` (11pm). Please note that the day window within a weekday starts at 6AM `hour = 6` and ends at 5AM `hour = 5` next day. See Introduction section [Forecast day window and weekdays](#forecast-day-window-and-weekdays)  
       &nbsp;
     - analysis[day_int].hour_analysis.**intensity_nr** `int`  
       Hour intensity_nr indicates how busy the venue is on a scale of 5, ranging from `-2` to `2`. When the venue is closed at the given hour it indicates `999`. See `intensity_txt` for the textual version of the same scale.  
       &nbsp;
     - analysis[day_int].hour_analysis.**intensity_txt** `string`  
       Hour intensity_txt indicates how busy the venue is on a scale of 5. See `intensity_nr` for the integer version of the same scale. The intensity is either `Low`, `Below average`, `Average`, `Above average`, or `High`. When the venue is closed at the given hour it indicates `Closed`.  
       &nbsp;
 - analysis[day_int].**peak_hours** `list`  
   List with peak objects, containing details of one or multiple peaks per day.  
  &nbsp;
     - analysis[day_int].peak_hours.**peak_start** `int`  
       Start hour of the peak, using the 24 hour notation.  
       &nbsp;
     - analysis[day_int].peak_hours.**peak_max** `int`  
       Hour of the day when the peak is at its maximum. Using the 24 hour notation.  
       &nbsp;
     - analysis[day_int].peak_hours.**peak_end** `int`  
       End hour of the peak, using the 24 hour notation.  
       &nbsp;
     - analysis[day_int].peak_hours.**peak_intensity** `int`  
       Intensity of the peak, rated from `1` (minimum) to `5` (maximum)  
       &nbsp;
     - analysis[day_int].peak_hours.**peak_delta_mean_week** `int`  
       Percentage how much the peak maximum is above the mean busyness of the week.  
       &nbsp;
 - analysis[day_int].**quiet_hours** `list`  
   List with quiet hours of the day. The hours are in 24 hour `int` notation.  
  &nbsp;
 - analysis[day_int].**surge_hours** `object`  
   Details at which hour most people enter (come) or leave the venue.
  &nbsp;
     - analysis[day_int].surge_hours.**most_people_come** `int`  
       Hour when most people come to the venue during the day window. The hours are in 24 hour `int` notation.  
       &nbsp;
     - analysis[day_int].surge_hours.**most_people_leave** `int`  
       Hour when most people leave to the venue during the day window. The hours are in 24 hour `int` notation.  
       &nbsp;
- **epoch_analysis** `int`  
 Epoch timestamp when the forecast was made.  
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
