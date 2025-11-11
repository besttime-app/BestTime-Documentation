
# Live foot-traffic data

> Returns Live foot-traffic data for a venue based on the venue name and address:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/live"

params = {
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
    'venue_name': 'McDonalds',
    'venue_address': 'Ocean Ave, San Francisco'
}

response = requests.request("POST", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request POST 'https://besttime.app/api/v1/forecasts/live?
api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&
venue_name=McDonalds&
venue_address=Ocean%20Ave%2C%20San%20Francisco'
```

```javascript
const params = new URLSearchParams({ 
  'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
  'venue_name': 'McDonalds',
  'venue_address': 'Ocean Ave, San Francisco'
});

fetch(`https://besttime.app/api/v1/forecasts/live?${params}`, {
  method: 'POST'
}).then(function(data) { 
  console.log(data); 
});
```

The 'live forecast' endpoint is used to get live information of the venue. Life forecasts are either created using the venue name and address, or the venue_id as input in the request. The response includes information regarding the live busyness at this moment compared to the forecasted busyness of the corresponding hour.  

When creating a live forecast the normal forecast for the venue will NOT be updated. Use one of the other New Forecast endpoints

<b>Highly recommended to read first:
- [BestTime tools beginners tutorial](https://blog.besttime.app/foot-traffic-nightlife-bars/)
- [BestTime Software API beginners tutorial](https://blog.besttime.app/beginners-guide-foot-traffic-data-software-api/)
- [HTML/ Javascript examples](#examples)
</b>  



### Input attributes Live foot traffic data

- **venue_id** `string` <span style="color:blue">RECOMMENDED/OPTIONAL</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues. To use the `venue_id` as input, the venue needs to be forecasted before. When the `venue_id` parameter is omitted the `venue_name` and `venue_address` parameters are required. We recommend using the venue_id for faster responses and when using a package subscription to stay within the subscription limits. 
 &nbsp;
- **venue_name** `string` <span style="color:blue">OPTIONAL</span>  
 Name of the venue (public business). Max input length `256` characters.  When then using the `venue_id` the `venue_name` and `venue_address` can be omitted. Highly recommend to use the `venue_id` (instead of name and address) for faster responses and when using a package subscription to stay within the subscription limits.
 &nbsp; 
- **venue_address** `string` <span style="color:blue">OPTIONAL</span>  
 Address of the venue (public business). The address does not have to be exact, but needs to be precise enough for the geocoder engine to find the correct venue. The more specific the address the higher chance the geocoder will find the venue. Max input length `1024` characters. The response object will also display the `venue_name` and `venue_address`, but is using the name and address of the geocoder's found venue. Check the `venue_name` and `venue_address` in the response object to verify if the correct venue has been forecasted.  
 &nbsp;
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Live endpoint: https://besttime.app/api/v1/forecast/live
</aside>

<aside class="notice">
HTTP method: POST
</aside>

<aside class="warning">
By default the API is limited to 10 requests per second. Contact us for higher limits.
</aside>  



> The above request returns JSON structured like this:

```json
{
    "status": "OK",
    "analysis": {
        "venue_forecasted_busyness": 85,
        "venue_forecast_busyness_available": true,
        "venue_live_busyness": 90,
        "venue_live_busyness_available": true,
        "venue_live_forecasted_delta": 5,
        "hour_start": 11,
        "hour_start_12": "11AM",
        "hour_end": 12,
        "hour_end_12": "12PM"
    },
    "venue_info": {
        "venue_current_gmttime": "Tuesday 2025-11-11 04:23PM",
        "venue_current_localtime": "Tuesday 2025-11-11 11:23AM",
        "venue_id": "ven_454e4e686e4a7046453659526b6f775a6c3673525158614a496843",
        "venue_name": "Empire State Building",
        "venue_address": "20 W 34th St. New York, NY 10001 United States",
        "venue_timezone": "America/New_York",
        "venue_open": "Open",
        "venue_dwell_time_min": 45,
        "venue_dwell_time_max": 120,
        "venue_dwell_time_avg": 82,
        "venue_lat": 40.7484405,
        "venue_lon": -73.98566439999999,
        "rating": 4.7,
        "reviews": 121628,
        "price_level": 0,
        "venue_open_close_v2": {
            "day_int": 1,
            "day_text": "Tuesday",
            "24h": [
                {
                    "opens": 11,
                    "closes": 22,
                    "opens_minutes": 0,
                    "closes_minutes": 0
                }
            ],
            "12h": [
                "11am–10pm"
            ],
            "special_day": null,
            "open_24h": false,
            "crosses_midnight": false
        }
    }
}
```

### Response attributes Live Forecast <a name="#response-attributes-live-forecast"></a>

- **analysis** `object`  
 Object with live analysis details.  
 &nbsp; 
 - analysis.**venue_forecasted_busyness** `int`  
   Forecasted busyness for this hour, based on the weekly forecast. Ranging from `0` to `100`.  
  &nbsp;
 - analysis.**venue_live_busyness** `int`  
   Live busyness at the venue for current, based on the weekly forecast.  
   In most cases, the live percentage will be between 0% and 100%. However, a value above 100%
   means it is busier than the highest forecasted peak of the week. E.g. 200% meaning it is two times as busy as the normal forecasted peak (100%) of the week. 
  &nbsp;
 - analysis.**venue_live_busyness_available** `bool`  
   Indicates if there is live data available for this venue at this moment.  
  &nbsp;
 - analysis.**venue_forecast_busyness_available** `bool`  
   Indicates if there is forecast data available for this venue at this moment. The forecast value can be used as the alternative when there is no live data available.
  &nbsp;
 - analysis.**venue_live_forecasted_delta** `int`  
   Indicates the difference of the current live busyness versus the forecasted busyness for this hour, in percentage. A negative number indicates that is is less busy then normal, while a positive number indicates that it is more busy than normal. Ranging from `-100` to `100`.  
  &nbsp;
 - analysis.**hour_start** `int`  
   Start hour of the current time window in 24 hour notation.  
  &nbsp;
 - analysis.**hour_start_12** `string`  
   Start hour of the current time window in 12 hour notation.  
  &nbsp;
 - analysis.**hour_end** `int`  
   End hour of the current time window in 24 hour notation.  
  &nbsp;
 - analysis.**hour_end_12** `string`  
   End hour of the current time window in 12 hour notation.  
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
 - venue_info.**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is the primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.  
  &nbsp;
 - venue_info.**venue_address** `string`  
   Address of the venue. This is the address of the venue as found by the geocoding lookup. Note this address could be different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_current_gmtttime** `string`  
   Time at the venue in Greenwich Mean Time.  
  &nbsp;
 - venue_info.**venue_current_localtime** `string`  
   Local time at the venue.  
  &nbsp;
 - venue_info.**venue_timezone** `string`  
  The timezone of the venue. E.g. `America/Los Angeles`.  
  &nbsp;
 - venue_info.**venue_open** `string`  
   Current open status of the venue. Either `"Open"` or `"Closed"`.  
  &nbsp;
 - venue_info.**venue_dwell_time_min** `int`  
   Minimum usual visitor dwell time in minutes, or `0` when not available.  
  &nbsp;
 - venue_info.**venue_dwell_time_max** `int`  
   Maximum usual visitor dwell time in minutes, or `0` when not available.   
  &nbsp;
 - venue_info.**venue_dwell_time_avg** `int`  
   Average usual visitor dwell time in minutes, or `0` when not available.   
  &nbsp;
 - venue_info.**rating** `float`
    Average rating of the venue. Possible values are `2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0`, or `0` when not available.
   &nbsp;
  - venue_info.**reviews** `int`
    Total number of reviews for the venue, or `0` when not available.
   &nbsp;
  - venue_info.**price_level** `int`
    Price level of the venue ranging from `1` (least expensive) to `5` (most expensive), or `0` when not available.
   &nbsp;
 - venue_info.**venue_lat** `float`
   Geographic latitude of the venue.
   &nbsp;
 - venue_info.**venue_lon** `float`
   Geographic longitude of the venue.
   &nbsp;
 - venue_info.**venue_open_close_v2** `object`
   Object with open and close times for the venue for the current day. The object contains `day_int`, `day_text`, two lists: `24h` and `12h`, and optional `special_day`. The `24h` list contains open and close times for the venue in 24 hour notation. The `12h` list contains open and close times for the venue in 12 hour notation. A venue can have multiple opening times per day.
   &nbsp;
   - venue_info.venue_open_close_v2.**day_int** `int`
     Day integer range `0` (Monday) to `6` (Sunday) for the current day.
     &nbsp;
   - venue_info.venue_open_close_v2.**day_text** `string`
     Day name for the current day. E.g. `"Tuesday"`.
     &nbsp;
   - venue_info.venue_open_close_v2.**24h** `list`
     List with objects describing each opening period in 24 hour notation. Every object contains `opens`, `opens_minutes`, `closes`, and `closes_minutes`.
     &nbsp;
   - venue_info.venue_open_close_v2.**12h** `list`
     List with open and close times for the venue in 12 hour notation.
     &nbsp;
   - venue_info.venue_open_close_v2.**special_day** `object|null`
     Optional object describing holiday/special-day overrides. Either `null` or an object with `message` and `name` fields when Google marks a day as special.
     &nbsp;
   - venue_info.venue_open_close_v2.**open_24h** `bool`
     Indicates if the venue is open 24 hours on this day.
     &nbsp;
   - venue_info.venue_open_close_v2.**crosses_midnight** `bool`
     Indicates if any opening period crosses midnight.
     &nbsp;