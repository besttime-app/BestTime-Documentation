# Venues Update

> Show a list of venues that our older than a specified amount of weeks. Optionally update each listed venue with a 'new foot traffic forecast':

```python
import requests
 
url = "https://besttime.app/api/v1/venues/update"

params = {
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b'
    'weeks': 2,
    'update': False,
    'foottraffic': 'with'
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/venues/update?
api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&
weeks=2&
update=false&
footttraffic=with'
```

```javascript
const params = new URLSearchParams({ 
  'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
  'weeks': 2,
  'update': false,
  'foottraffic': 'with'
});

fetch(`https://besttime.app/api/v1/venues/update${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes Venues Update

The 'Venues Update' endpoint returns list of venues that our older than a specified amount of weeks for the given 'api_key_private'. Optionally update each listed venue with a 'new foot traffic forecast'. This endpoint can also be filtered by collection_id or a geographical bounding box. 

- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-reference)  
 &nbsp; 
- **weeks** `int` <span style="color:blue">OPTIONAL</span> 
 Return only venues that have not been updated more than the selected number of `weeks`. Default is `2`. Minimum is `0`.  
 &nbsp; 
- **update** `bool` <span style="color:blue">OPTIONAL</span> 
  Automatically update all returend venues by pushing them to the 'New foot traffic forecast' API endpoint (normal API credits apply for each venue). Default is `false` (not updating).  
 &nbsp; 
- **foottraffic** `string` <span style="color:blue">OPTIONAL</span> 
  Return only venues with or without foot traffic data. Options `with`, `without`, `all`. `with` will return only venues that had foot traffic forecast data last update. `without` will only return venues that did not have foot traffic forecast data last update. `all` will return all matching venues regardless if they have foot traffic data. Default is `with`. Not all venues that have been added to your BestTime account have foot traffic data. Also venues without foot traffic data will be stored in your account. By default, these venues will not be shown and updated to save API credits (`with`). Sometimes it can be usefull to also update previously failed forecast - when e.g. venues are re-opened or are getting more popular (and therefore might have foot traffic at this moment).  
 &nbsp; 
- **collection_id** `string` <span style="color:blue">OPTIONAL</span>  
Return only venues within a collection. See more info on [Collections](#venue-collections)  
 &nbsp;
- **lat_min** `float` <span style="color:blue">OPTIONAL</span>  
   Minimum latitude of the bounding box (South-West). `lat_min` must be combined with `lat_max`, `lng_min` and `lng_max`. The bounding box cannot be combined with the circle parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp; 
- **lng_min** `float` <span style="color:blue">OPTIONAL</span>  
   Minimum longitude of the bounding box (South-West). `lng_min` must be combined with `lng_max`, `lat_min` and `lat_max`.  
  &nbsp; 
- **lat_max** `float` <span style="color:blue">OPTIONAL</span>  
   Maximum latitude of the bounding box (North-East). `lat_max` must be combined with `lat_min`, `lng_min` and `lng_max`.   
  &nbsp; 
- **lng_max** `float` <span style="color:blue">OPTIONAL</span>  
   Maximum longitude of the bounding box (North-East). `lng_max` must be combined with `lng_min`, `lat_min` and `lat_max`. 
  &nbsp; 
<aside class="notice">
Venues update endpoint: https://besttime.app/api/v1/venues/update
</aside>

<aside class="notice">
HTTP method: GET
</aside>

<aside class="warning">
API Credit usage per API call for this endpoint depends on the number of returned venues and your plan. See 'API key credits' for more information.
</aside>

> The above request returns a JSON response like this (this example only contains a list with one venue):

```json
 {
   "message": "Venues with foot traffic data older than 2 week(s). Listed venues will not be updated. Set 'update=true' to create a new foot traffic forecast for each individual venue (normal 'new foot traffic forecast' API credits apply for each venue)",
    "status": "OK",
    "venues": [
        [
           "1201 Ocean Ave San Francisco, CA 94112 United States",
            "ven_51387131543761435650505241346a394a6432395362654a496843",
            "2021-03-05 04:37AM"
        ],....
    ],
    "venues_n": 298
 }
```


### Response attributes Query Venues
The JSON response will contain a `list` with venue `objects`.

- **venues[N]** `object` 
 Each venue object contains detailed venue information.
 - venues[N].**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup. Note this name could be slightly different than the `venue_address` used as input.  
  &nbsp;
 - venues[N].**venue_address** `string`  
   Address of the venue. This is the address of the venue as found by the geocoding lookup. Note this address could be different than the `venue_address` used as input.  
  &nbsp;
 - venues[N].**venue_forecasted** `Bool`  
   When a venue has been successfully forecasted the value will be `true`. The value will be `false` if the venue has been found by the geocoder, but the venue could not be forecasted.  
  &nbsp;
 - venues[N].**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is the primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.
  &nbsp;
 - venue[N].**forecast_updated_on** `DateTime string`  
   Date and time of the last foot traffic forecast.

