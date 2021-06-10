
# Live foot-traffic data

> Returns Live foot-traffic data for a venue based on the venue name and address:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/live"

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
curl --location --request POST 'https://besttime.app/api/v1/forecasts/live?
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

fetch(`https://besttime.app/api/v1/forecasts/live?${params}`, {
  method: 'POST'
}).then(function(data) { 
  console.log(data); 
});
```

The 'live forecast' endpoint is used to get live information of the venue. Life forecasts are either created using the venue name and address, or the venue_id as input in the request. The response includes information regarding the live busyness at this moment compared to the forecasted busyness of the corresponding hour.  

When creating a live forecast the normal forecast for the venue will NOT be updated. Use one of the other New Forecast endpoints


### Input attributes Live foot traffic data

- **venue_name** `string` <span style="color:blue">OPTIONAL</span>  
 Name of the venue (public business). When then using the `venue_id` the `venue_name` and `venue_address` can be omitted.  
 &nbsp; 
- **venue_address** `string` <span style="color:blue">OPTIONAL</span>  
 Address of the venue (public business). The address does not have to be exact, but needs to be precise enough for the geocoder engine to find the correct venue. The more specific the address the higher chance the geocoder will find the venue. The response object will also display the `venue_name` and `venue_address`, but is using the name and address of the geocoder's found venue. Check the `venue_name` and `venue_address` in the response object to verify if the correct venue has been forecasted.  
 &nbsp;
- **venue_id** `string` <span style="color:blue">OPTIONAL</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues. To use the `venue_id` as input, the venue needs to be forecasted before. When the `venue_id` parameter is omitted the `venue_name` and `venue_address` parameters are required.  
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
    "analysis": {
        "venue_forecasted_busyness": 60,
        "venue_live_busyness": 20,
        "venue_live_busyness_available": true,
        "venue_forecast_busyness_available": true,   
        "venue_live_forecasted_delta": -40
    },
    "status": "OK",
    "venue_info": {
        "venue_current_gmttime": "Friday 2021-04-23 07:19AM",
        "venue_current_localtime": "Friday 2021-04-23 03:19PM",
        "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles",
        "venue_dwell_time_min": 20,
        "venue_dwell_time_max": 60,
        "venue_dwell_time_avg": 40
    }
}
```

### Response attributes Live Forecast <a name="responseattributesnewforecast"></a>

- **analysis** `object`  
 Object with live analysis details.  
 &nbsp; 
 - analysis.**venue_forecasted_busyness** `int`  
   Forecasted busyness for this hour, based on the weekly forecast. Ranging from `0` to `100`.  
  &nbsp;
 - analysis.**venue_live_busyness** `int`  
   Live busyness at the venue for current, based on the weekly forecast. Ranging from `0` to `200` percent. 
   In most cases the live percentage will be 100% or lower. However if the value is above 100% it 
   means it is more busy than the highest forecasted peak of the week. E.g. 200% meaning it is two times more busy than the normal forecasted peak of the week. 
  &nbsp;
 - analysis.**venue_live_busyness_available** `bool`  
   Indicates if there is live data available for this venue at this moment.  
  &nbsp;
 - analysis.**venue_forecast_busyness_available** `bool`  
   Indicates if there is forecast data available for this venue at this moment. The forecast value can be used as alternative when there is no live data available.
  &nbsp;
 - analysis.**venue_live_forecasted_delta** `int`  
   Indicates the difference of the current live busyness versus the forecasted busyness for this hour, in percentage. A negative number indicates that is is less busy then normal, while a positive number indicates that it is more busy than normal. Ranging from `-100` to `100`.  
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
 - venue_info.**venue_current_gmtttime** `string`  
   Time at the venue in Greenwich Mean Time.  
 - venue_info.**venue_current_localtime_iso** `string`  
   Local time at the venue.  
  &nbsp;
 - venue_info.**venue_timezone** `string`  
  The timezone of the venue. E.g. `America/Los Angeles`.  
  &nbsp;
 - venue_info.**venue_dwell_time_min** `int`  
   Minimum usual visitor dwell time in minutes, or `null` when not available.  
  &nbsp;
 - venue_info.**venue_dwell_time_max** `int`  
   Maximum usual visitor dwell time in minutes, or `null` when not available.   
  &nbsp;
 - venue_info.**venue_dwell_time_avg** `int`  
   Average usual visitor dwell time in minutes, or `null` when not available.   
  &nbsp;