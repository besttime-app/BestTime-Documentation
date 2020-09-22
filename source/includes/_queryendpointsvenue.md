## Query venue

> Query a single venue:

```python
import requests
import json

url = "https://besttime.app/api/v1/venues/ven_51387131543761435650505241346a394a6432395362654a496843"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754'
}

response = requests.request("GET", url, params=params)

data = json.loads(response.text)

print(data)
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/venues/en_51387131543761435650505241346a394a6432395362654a496843&
api_key_public=pub_e11661721b084d36b8f469a2c012e754'
```

```javascript
$.ajax({
"url": "https://besttime.app/api/v1/venues/ven_51387131543761435650505241346a394a6432395362654a496843?api_key_public=pub_e11661721b084d36b8f469a2c012e754",
"method": "GET"
}).done(function (response) {
    console.log(response);
});
```

### Input attributes Query Venue

The 'query venue' endpoint is used to retrieve information about the venue. It does not contain forecasted data, except the day rankings for a week. This query endpoint requires the private API key. Although the private API keys is used, this endpoint will be charged with query credits.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 

- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-keys)  
 &nbsp; 

<aside class="notice">
Query venue endpoint: https://BestTime.app/api/v1/venues/<venue_id>
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON response like this:

```json
{
    "epoch_analysis": 1585875838,
    "forecast_updated_on": "Fri, 03 Apr 2020 01:03:58 GMT",
    "status": "OK",
    "venue_forecasted": true,
    "venue_info": {
        "venue_address": "1201 Ocean Ave San Francisco, CA 94112",
        "venue_current_gmttime": "Fri, 03 Apr 2020 03:03:51 GMT",
        "venue_current_localtime_iso": "2020-04-02T20:03:51.063663-07:00",
        "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
        "venue_lat": 37.7235448,
        "venue_lng": -122.455458,
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles"
    }
}
```


### Response attributes Query Venue
The JSON response will contain detailed venue information.

- **epoch_analysis** `int`  
 Epoch timestamp when the forecast was made.  
 &nbsp; 
- **forecast_updated_on** `TimeZone Aware DateTime string`  
 Date and time (Time Zone aware) of the original forecast.  
 &nbsp; 
- **status** `string`  
 Status of the response. Either `OK` or `Error`.  
 &nbsp; 
- **venue_forecasted** `bool`  
  When a venue has been successfully forecasted the value will be `true`. The value will be `false` if the venue has been found by the geocoder, but the venue could not be forecasted.  
 &nbsp; 
- **venue_info** `object`  
 Details of the forecasted venue.  
 &nbsp; 
  - venue_info.**venue_address** `string`  
   Address of the venue. This is the address of the venue as found by the geocoding lookup. Note this address could be different than the `venue_address` used as input.  
  - venue_info.**venue_current_gmtttime** `string`  
   Time at the venue in Greenwich Mean Time. Adjusting the `hour_step` and `day_step` will also alter this time.  
  - venue_info.**venue_current_localtime_iso** `string`  
   Local time at the venue in ISO standard format.
  &nbsp;
 - venue_info.**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is the primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.
  &nbsp;
 - venue_info.**venue_lat** `float`  
   Geographic latitude of the venue.
  &nbsp;
 - venue_info.**venue_lng** `float`  
   Geographic longitude of the venue.
  &nbsp;
  - venue_info.**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup. Note this name could be slightly different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_timezone** `string`  
   The timezone of the venue. E.g. `America/Los Angeles`  
  &nbsp;
