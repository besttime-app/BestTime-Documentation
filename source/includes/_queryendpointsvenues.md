## Query all venues

> Query list of all forecasted venues:

```python
import requests
import json

url = "https://beta.besttime.app/api/v1/venues"

params = {
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b'
}

response = requests.request("GET", url, params=params)

data = json.loads(response.text)

print(data)
```

```shell
# cURL
curl --location --request GET 'https://beta.besttime.app/api/v1/venues?
api_key_private=pri_50990bf1f8828f6abbf6152013113c6b'
```

```javascript
$.ajax({
"url": "https://beta.besttime.app/api/v1/venues?api_key_private=pri_50990bf1f8828f6abbf6152013113c6b",
"method": "GET"
}).done(function (response) {
    console.log(response);
});
```

### Input attributes Query All Venues

The 'query venues' endpoint is used to retrieve a list with all previously forecasted venues. This query endpoint requires the private API key. Although the private API keys is used, this endpoint will be charged with query credits.

- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-keys)  
 &nbsp; 

<aside class="notice">
Query venues endpoint: https://beta.besttime.app/api/v1/venues
</aside>

<aside class="notice">
HTTP method: GET
</aside>

<aside class="warning">
API Credit usage per API call for this endpoint depends on the amount of returned venues and your plan. See 'API key credits' for more information.
</aside>

> The above request returns a JSON response like this (this example only contains a list with one venue):

```json
[
    {
        "venue_address": "1201 Ocean Ave San Francisco, CA 94112 United States",
        "venue_forecasted": true,
        "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
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

