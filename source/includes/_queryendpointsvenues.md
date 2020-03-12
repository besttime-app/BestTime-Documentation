## Query venues

> Query list of all forecasted venues:

```python
import requests
import json

url = "https://BestTime.app/api/v1/query/venues/"

headers = {
    'Content-Type': 'application/json'
}

payload = json.dumps({
    "api_key_private": "e267713ecda84c77a055294dbb12c6d4"
})

response = requests.request("POST", url, headers=headers, data = payload)

response_dict = json.loads(response.text.encode('utf8'))
```

```shell
# cURL
curl --location --request POST 'https://BestTime.app/api/v1/query/venues/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "api_key_private": "e267713ecda84c77a055294dbb12c6d4"
}	'
```

```javascript
var settings = {
  "url": "https://BestTime.app/api/v1/query/venues/",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
      "api_key_private": "e267713ecda84c77a055294dbb12c6d4"
    }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

### Input attributes Query Venues

The 'query venues' endpoint is used to retrieve a list with all previously forecasted venues. This query endpoint requires the private API key. Although the private API keys is used, this endpoint will be charged with query credits.

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
[
    {
        "epoch_analysis": 1583911633,
        "updated_on": "Wed, 11 Mar 2020 07:27:14 GMT",
        "venue_address": "1201 Ocean Ave San Francisco, CA 94112 United States",
        "venue_forecasted": true,
        "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
        "venue_lat": 37.7235448,
        "venue_lng": -122.455458,
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles",
        "venue_week_rank_max": [
            5,
            5,
            1,
            3,
            7,
            6,
            2
        ],
        "venue_week_rank_mean": [
            5,
            4,
            2,
            2,
            3,
            6,
            7
        ]
    }
]
```


### Response attributes Query Venues
The JSON response will contain a `list` with venue `objects`.

- **venue[N]** `object` 
 Each venue object contains detailed venue information.
 - venue[N].**epoch_analysis** `int`  
   Epoch timestamp when the forecast was made.  
  &nbsp;
 - venue[N].**forecast_updated_on** `TimeZone Aware DateTime string`  
  Date and time (Time Zone aware) of the original forecast.  
  &nbsp;
 - venue[N].**venue_address** `string`  
   Address of the venue. This is the address of the venue as found by the geocoding lookup. Note this address could be different than the `venue_address` used as input.  
  &nbsp;
 - venue[N].**venue_forecasted** `Bool`  
   When a venue has been succesfully forecasted the value will be `true`. The value will be `false` if the venue has been found by the geocoder, but the venue could not be forecasted.
  &nbsp;
 - venue[N].**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is the primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.
  &nbsp;
 - venue[N].**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup. Note this name could be slightly different than the `venue_address` used as input.  
  &nbsp;
 - venue[N].**venue_timezone** `string`  
   The timezone of the venue. E.g. `America/Los Angeles`  
  &nbsp;
 - venue[N].**day_rank_max** `list`  
    Day ranking list based on the maximum busyness of the day. It contains `int` elements ranging from `1` to `7`. E.g. `2` indicates the 2nd most surge day of the week. The first element represents Monday, and the last element represents Sunday.  
    &nbsp;
 - venue[N].**day_rank_mean** `list`  
    Day ranking list based on mean busyness (total volume) of the day. It contains `int` elements ranging from `1` to `7`. E.g. `7` indicates the least surge day of the week. The first element represents Monday, and the last element represents Sunday.  
    &nbsp;

