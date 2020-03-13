## Query venue

> Query a single venue:

```python
import requests
import json

url = "https://BestTime.app/api/v1/query/venue/"

headers = {
    'Content-Type': 'application/json'
}

payload = json.dumps({
  	"venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
    "api_key_private": "e267713ecda84c77a055294dbb12c6d4"
})

response = requests.request("POST", url, headers=headers, data = payload)

response_dict = json.loads(response.text.encode('utf8'))
```

```shell
# cURL
curl --location --request POST 'https://BestTime.app/api/v1/query/venue/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
  "api_key_private": "e267713ecda84c77a055294dbb12c6d4"
}	'
```

```javascript
var settings = {
  "url": "https://BestTime.app/api/v1/query/venue/",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    	"venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
      "api_key_private": "e267713ecda84c77a055294dbb12c6d4"
    }),
};

$.ajax(settings).done(function (response) {
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
Query venues endpoint: https://BestTime.app/api/v1/query/venues/
</aside>

<aside class="notice">
HTTP method: POST
</aside>


> The above request returns a JSON response like this:

```json
{
    "analysis": {
        "week_info": {
            "day_rank_max": [
                5,
                5,
                1,
                3,
                7,
                6,
                2
            ],
            "day_rank_mean": [
                5,
                4,
                2,
                2,
                3,
                6,
                7
            ]
        }
    },
    "epoch_analysis": 1583990338,
    "forecast_updated_on": "Thu, 12 Mar 2020 05:18:59 GMT",
    "status": "OK",
    "venue_forecasted": true,
    "venue_info": {
        "venue_address": "1201 Ocean Ave San Francisco, CA 94112 United States",
        "venue_current_gmttime": "Thu, 12 Mar 2020 05:49:15 GMT",
        "venue_current_localtime_iso": "2020-03-11T22:49:15.899800-07:00",
        "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
        "venue_lat": 37.7235448,
        "venue_lng": -122.455458,
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles"
    }
}
```


### Response attributes Query Venue
The JSON response will contain detailed venue information.

- **analysis** `object`  
 Containing the all the included analytics like 'peak_hours', 'busy_hours', etc for the given day. 
 - analysis.**week_info** `object`  
   Details about the week    
  &nbsp;
     - analysis.week_info.**day_rank_max** `list`  
       Day ranking list based on the maximum busyness of the day. It contains `int` elements ranging from `1` to `7`. E.g. `2` indicates the 2nd most busy day of the week. The first element represents Monday, and the last element represents Sunday.  
       &nbsp;
     - analysis.week_info.**day_rank_mean** `list`  
       Day ranking list based on mean busyness (total volume) of the day. It contains `int` elements ranging from `1` to `7`. E.g. `7` indicates the least busy day of the week. The first element represents Monday, and the last element represents Sunday.  
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
