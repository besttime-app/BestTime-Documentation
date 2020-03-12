## Query all venues

> Query list of all forecasted venues:

```python
import requests
import json

url = "https://BestTime.app/api/v1/query/allvenues/"

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
curl --location --request POST 'https://BestTime.app/api/v1/query/allvenues/' \
--header 'Content-Type: application/json' \
--data-raw '{
  "api_key_private": "e267713ecda84c77a055294dbb12c6d4"
}	'
```

```javascript
var settings = {
  "url": "https://BestTime.app/api/v1/query/allvenues/",
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

### Input attributes Query All Venues

The 'query venues' endpoint is used to retrieve a list with all previously forecasted venues. This query endpoint requires the private API key. Although the private API keys is used, this endpoint will be charged with query credits.

- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-keys)  
 &nbsp; 

<aside class="notice">
Query venues endpoint: https://BestTime.app/api/v1/query/allvenues/
</aside>

<aside class="notice">
HTTP method: POST
</aside>


> The above request returns a JSON response like this (this example only contains a list with one venue):

```json
[
    {
        "venue_address": "1201 Ocean Ave San Francisco, CA 94112 United States",
        "venue_forecasted": true,
        "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
        "venue_name": "McDonald's"
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
 - venue[N].**venue_address** `string`  
   Address of the venue. This is the address of the venue as found by the geocoding lookup. Note this address could be different than the `venue_address` used as input.  
  &nbsp;
 - venue[N].**venue_forecasted** `Bool`  
   When a venue has been successfully forecasted the value will be `true`. The value will be `false` if the venue has been found by the geocoder, but the venue could not be forecasted.  
  &nbsp;
 - venue[N].**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is the primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.
  &nbsp;
 - venue[N].**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup. Note this name could be slightly different than the `venue_address` used as input.  
  &nbsp;

