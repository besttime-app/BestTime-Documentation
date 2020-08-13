## Query filtered venues (Radar)

> Filter forecasted venues on busyness, location, type, day, and time. 

```python
import requests
import json

url = "https://besttime.app/api/v1/venues/filter"

params = {
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
    'busy_min': 50,
    'busy_max': 100,
    'hour_min': 18,
    'hour_max': 23,
    'now': False,
    'live': False,
    'types': ['BAR','CAFE','NIGHTCLUB'],
    'lat': 51.5121172,
    'lng': -0.126173,
    'radius': 2000
}

response = requests.request("GET", url, params=params)

data = json.loads(response.text)

print(data)
```

<!-- ```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/venues?
    api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&
    busy_min=50&
    busy_max=100,
    hour_min=18,
    hour_max=23,
    now=false,
    live=false,
    types': ['BAR','CAFE','NIGHTCLUB'],
    lat': 51.5121172,
    lng': -0.126173,
    radius': 2000
``` -->

```javascript
var settings = {
    "url": "https://besttime.app/api/v1/venues",
    "data": {
            'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
            'busy_min': 50,
            'busy_max': 100,
            'hour_min': 18,
            'hour_max': 23,
            'now': false,
            'live': false,
            'types': ['BAR','CAFE','NIGHTCLUB'],
            'lat': 51.5121172,
            'lng': -0.126173,
            'radius': 2000
    },
    "method": "GET"
};

$.ajax(settings).done(function (response) {
    console.log(response);
});
```

<aside class="warning">
This API endpoint is currently in beta and expected to be released in August 2020.
</aside>

### Input attributes Venue Filter

The 'venue filter' endpoint will return all venues and the raw forecasted busyness data that meet the filter requirements. Venues can be filtered on how busy they are, on  location, type of venue, day & time range, or a combination. This could be useful to for e.g. find all busy bars, cafes and nightclubs, between 6pm and 11pm in a specific neighborhood. The filter will only return venues that are forecasted with the given private API key.

This query endpoint requires the private API key. Although the private API keys is used, this endpoint will be charged with query credits.

The BestTime ['Radar'](https://besttime.app/api/v1/radar/filter) tool is using the same API endpoint to show all venues that meet the filter criteria on a (heat)map (scheduled to be released in August 2020).

The endpoint will only return venues that have been forecasted before with the provided `api_key_private`. The user can manually add each desired venue individually through the BestTime API, or can use an external API service with public business (like Google Maps Places Nearby search, Here.com, Fouresquare Venues, or Factual Places). Using the external service places in a certain area can be discovered and the results (venue name and address) can be fed into the BestTime API. 

To prevent manually adding all venues in a specific area (e.g. neighborhood or city) the 'Add Area' tool can be used (expected to be released in August 2020). Using this tool the user can define a geographical bounding box, select multiple desired types of venues (e.g. supermarkets, gyms, restaurants, etc). Under the hood it uses the Google Maps Nearby API to discover venues in the defined area (you will need a Google Maps API key). This geocoder has currently the biggest database and gives the best results.

![Radar tool (Venue filter)](images/radar-venue-filter-small.jpg)

- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. The endpoint will only return venues that are forecasted with this private API key.  See more info on [API keys](#api-keys)  
 &nbsp;
- **busy_min** `int` <span style="color:blue">OPTIONAL</span>  
Minimum busyness for the filtered venues, ranging from `0` to `100` procent. Matches the filter if at least <b>one</b> of the selected hour(s) is at or above the minimum selected busyness.  
 &nbsp;
- **busy_max** `int` <span style="color:blue">OPTIONAL</span>  
Maximum busyness for the filtered venues, ranging from `0` to `100` procent. Matches the filter if <b>all</b> selected hour(s) are at or below the selected maximum busyness.  
 &nbsp;
- **hour_min** `int` <span style="color:blue">OPTIONAL</span>  
Start hour, using the 24 hour notation. Ranging from `0` to `24` hour within the day window.  See [Forecast day window and weekdays](#forecast-day-window-and-weekdays). Cannot be used in combination with the `now` and `live` parameters set to be `true`.  
 &nbsp;
- **hour_max** `int` <span style="color:blue">OPTIONAL</span>  
Start hour, using the 24 hour notation. Ranging from `0` to `24` hour within the day window.  See [Forecast day window and weekdays](#forecast-day-window-and-weekdays). Cannot be used in combination with the `now` and `live` parameters set to be `true`.  
 &nbsp;
- **day_int** `int` <span style="color:blue">OPTIONAL</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday). Will default to current day in local time of the first found venue that meets the filter. Cannot be used in combination with the `now` and `live` parameters set to be `true`.
 &nbsp; 
- **now** `bool` <span style="color:blue">OPTIONAL</span>  
 Sets the time and day filter to the current day and hour in local time. The local time of the first venue is taken that matches the filter criteria. Cannot be used in combination with the `live`, `day_int`, `hour_min`, and `hour_max` parameters.  
 &nbsp; 
- **live** `bool` <span style="color:blue">OPTIONAL</span>  
 Sets the time and day filter to the current day and hour in local time, and will display the live busyness. Venues without live data will be filtered out. The local time of the first venue is taken that matches the filter criteria. Cannot be used in combination with the `now`, `day_int`, `hour_min`, and `hour_max` parameters.  
 &nbsp; 
- **types** `list` <span style="color:blue">OPTIONAL</span>  
 Filters on one or more venue types. All types are selected if the `types` parameter is ommited. Possible types are `['APPAREL', 'ARTS', 'BANKING', 'BAR', 'BOTANICAL_GARDEN', 'CAFE', 'CAR_RENTAL', 'CHURCH', 'CITY_HALL', 'COFFEE', 'DENTIST', 'DOCTOR', 'EMBASSY', 'EVENT_VENUE', 'FAST_FOOD', 'FOOD_AND_DRINK', 'FOOD_DELIVERY', 'GAS_STATION', 'GOVERNMENT', 'GROCERY', 'LODGING','MARKET', 'MOVIE_THEATER', 'MUSEUM', 'Other', 'PARK', 'PERFORMING_ARTS', 'PERSONAL_CARE', 'PHARMACY', 'PUBLIC_TRANSIT', 'RESTAURANT', 'SCHOOL', 'SHOPPING', 'SKILL_INSTRUCTION', 'SPA', 'SPORTS_COMPLEX', 'SUPERMARKET', 'TEA', 'TOURIST_DESTINATION', 'VISITOR_CENTER']`  
 &nbsp; 
- **lat** `float` <span style="color:blue">OPTIONAL</span>  
   Geographic latitude of the search circle. `lat` must be combined with `lng`, and `radius`. The search circle cannot be combined with the bounding box parameters.  
  &nbsp;
- **lng** `float` <span style="color:blue">OPTIONAL</span>  
   Geographic longitude of the search circle.  `lng` must be combined with `lat`, and `radius`. The search circle cannot be combined with the bounding box parameters.  
  &nbsp; 
- **radius** `int` <span style="color:blue">OPTIONAL</span>  
   Radius of the search circle in meter.  `radius` must be combined with `lat`, and `lng`. The search circle cannot be combined with the bounding box parameters.  
  &nbsp; 
- **lat_min** `float` <span style="color:blue">OPTIONAL</span>  
   Minimum latitude of the bounding box (South-West). `lat_min` must be combined with `lat_max`, `lng_min` and `lng_max`. The bounding box cannot be combined with the circle parameters.  
  &nbsp; 
- **lng_min** `float` <span style="color:blue">OPTIONAL</span>  
   Minimum longitude of the bounding box (South-West). `lng_min` must be combined with `lng_max`, `lat_min` and `lat_max`. The bounding box cannot be combined with the circle parameters.  
  &nbsp; 
- **lat_max** `float` <span style="color:blue">OPTIONAL</span>  
   Maximum latitude of the bounding box (North-East). `lat_max` must be combined with `lat_min`, `lng_min` and `lng_max`. The bounding box cannot be combined with the circle parameters.  
  &nbsp; 
- **lng_max** `float` <span style="color:blue">OPTIONAL</span>  
   Maximum longitude of the bounding box (North-East). `lng_max` must be combined with `lng_min`, `lat_min` and `lat_max`. The bounding box cannot be combined with the circle parameters.  
  &nbsp; 

<aside class="notice">
Query filtered venues endpoint: https://BestTime.app/api/v1/venues/filter
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON response like this (this example only contains a list with one venue):

```json
{
  "status": "OK", 
  "venues": [
    {
      "day_int": 0, 
      "day_raw": [
        0, 
        20, 
        80, 
        80, 
        20, 
        0
      ], 
      "venue_address": "61 Piccadilly Mayfair, London W1J 0DY United Kingdom", 
      "venue_id": "ven_386d55494f76464873784752676b6445593949455752594a496843", 
      "venue_lat": 51.5079836, 
      "venue_lng": -0.1404946, 
      "venue_name": "Caffe Concerto Green Park"
    }, 
    {
      "day_int": 0, 
      "day_raw": [
        40, 
        60, 
        60, 
        0, 
        0, 
        0
      ], 
      "venue_address": "14 Riding House St Fitzrovia, London W1W 7HR United Kingdom", 
      "venue_id": "ven_6372542d36476a4a59686d52676b646155646e713661514a496843", 
      "venue_lat": 51.5183082, 
      "venue_lng": -0.1415526, 
      "venue_name": "The Great Thai Restaurant"
    }
  ]
}
```


### Response attributes Query Venues
The JSON response will contain a `list` with venue `objects`.

- **venues[N]** `object` 
 Each venue object contains venue information and busyness data.  
  &nbsp;
  - venues[N].**day_int** `int`  
    Day integer range `0` (Monday) to `6` (Sunday)  
    &nbsp;
  - venues[N].**day_raw** `list`  
    List of raw busyness data for each hour of the day, or within the selected hour range. The list contains percentages ranging from `0` to `100`. Indicating the busyness percentage. Percentages are based on historical visits for the given hour, relative to the biggest peak of the week for this venue. When the `now` or `live` parameter is `true` the list will contain one `int` for the current hour in the local time.  
    &nbsp;
  - venues[N].**venue_address** `string`  
   Address of the venue. This is the address of the venue as found by the geocoding lookup.  
  &nbsp;
  - venues[N].**venue_lat** `float`  
   Geographic latitude of the venue.  
  &nbsp;
  - venues[N].**venue_lng** `float`  
   Geographic longitude of the venue.  
  &nbsp;
  - venues[N].**venue_id** `string`  
   Unique BestTime.app venue id.  
  &nbsp;
  - venues[N].**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup.  
  &nbsp;
- **status** `string` 
 Status of the response. Either `OK` or `error`.
