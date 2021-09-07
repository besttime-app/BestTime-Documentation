# Query filtered venues (Radar)

> Filter forecasted venues on busyness, location, type, day, and time. 

```python
import requests
 
url = "https://besttime.app/api/v1/venues/filter"

params = {
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
    'busy_min': 50,
    'busy_max': 100,
    'hour_min': 18,
    'hour_max': 23,
    'busy_conf':'any',
    'types': ['BAR','CAFE','RESTAURANT'],
    'lat': 51.5121172,
    'lng': -0.126173,
    'radius': 2000,
    'order_by': ['day_rank_max','reviews'],
    'order': ['desc','desc'],
    'foot_traffic': 'both',
    'limit': 20,
    'page': 0
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/venues/filter?api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&busy_min=50&busy_max=100&hour_min=18&hour_max=23&hour_conf=any&types=BAR,CAFE,RESTAURANT&lat=51.5121172&lng=-0.126173&radius=2000&order_by=day_rank_max%2Creviews&order=asc%2Cdesc&foot_traffic=both&limit=20&page=0'
```

```javascript
const params = new URLSearchParams({ 
 'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
    'busy_min': 50,
    'busy_max': 100,
    'busy_conf':'any',
    'hour_min': 18,
    'hour_max': 23,
    'types': ['BAR','CAFE','RESTAURANT'],
    'lat': 51.5121172,
    'lng': -0.126173,
    'radius': 2000,
    'order_by': ['day_rank_max','reviews'],
    'order': ['desc','desc'],
    'foot_traffic': 'both',
    'limit': 20,
    'page': 0
});

fetch(`https://besttime.app/api/v1/venues/filter?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```


### Input attributes Venue Filter

The 'venue filter' endpoint will return all venues and foot traffic data that meet the filter requirements. Venues can be filtered on how busy they are, on  location, type of venue, day & time range, etc, or a combination. This could be useful to for e.g. find all busy bars, cafes and nightclubs, between 6pm and 11pm in a specific neighborhood. The filter will only return venues that are forecasted before with the given private API key.

The BestTime Radar tool is using the same API endpoint to show all venues that meet the filter criteria on a (heat)map.

The endpoint will only return venues that have been forecasted before with the provided `api_key_private`. The user can manually add each desired venue individually through the BestTime API, or can use an external API service with public business (like Google Maps Places Nearby search, Here.com, Fouresquare Venues, or Factual Places). Using the external service places in a certain area can be discovered and the results (venue name and address) can be fed into the BestTime API. 

To prevent manually adding all venues in a specific area (e.g. neighborhood or city) the 'Add Area' or 'Venue Search' tool can be used. Using the 'Add Area' tool the user can define a geographical bounding box, select multiple desired types of venues (e.g. supermarkets, gyms, restaurants, etc). Under the hood it uses the Google Maps Nearby API to discover venues in the defined area (you will need a Google Maps API key). This geocoder has currently the biggest database and gives the best results.


<b>Highly recommended to read first:
- [BestTime tools beginners tutorial](https://blog.besttime.app/foot-traffic-nightlife-bars/)
- [BestTime Software API beginners tutorial](https://blog.besttime.app/beginners-guide-foot-traffic-data-software-api/)
</b>

Radar tool (which is using this 'venue filter' endpoint) 
<a href="images/radar-venue-filter-small.jpg" target="_blank">
  <img alt="Radar tool (Venue filter)" src="images/radar-venue-filter-small.jpg">
</a>

- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. The endpoint will only return venues that are forecasted with this private API key.  See more info on [API keys](#api-reference)  
 &nbsp;
- **collection_id** `string` <span style="color:blue">OPTIONAL</span>  
Filters on venues within a collection. See more info on [Collections](#venue-collections)
 &nbsp;
- **busy_min** `int` <span style="color:blue">OPTIONAL</span>  
Minimum busyness for the filtered venues, ranging from `0` to `100` procent.  Use `busy_conf` parameter to change the filter method. Warning: Currently the `busy_min` filter is applied after the `limit` parameter. We are currently working on a fix. A temporarily solution is to not set the 'limit' value in the API, and limit the number of venues client side.
 &nbsp;
- **busy_max** `int` <span style="color:blue">OPTIONAL</span>  
Maximum busyness for the filtered venues, ranging from `0` to `100` procent. Use `busy_conf` parameter to change the filter method. Warning: Currently the `busy_max` filter is applied after the `limit` parameter. We are currently working on a fix. A temporarily solution is to not set the 'limit' value in the API, and limit the number of venues client side. 
 &nbsp;
- **busy_conf** `string` <span style="color:blue">OPTIONAL</span>  
Selects how `busy_min` and `busy_max` filters on busyness percentage. Possible options are `any` or `all`. Defaults to  `any`. `any` will return venues when at least one of the (selected) hours matches the `busy_min` and/or `busy_max` filter(s). `all` will return venues when all (selected) hours match the `busy_min` and/or `busy_max` filter(s). Use the `hour_min` and/or `hour_max` parameters to select specific hours were the `busy_min` and/or `busy_max` filters are applied on.  
 &nbsp;
- **foot_traffic** `string` <span style="color:blue">OPTIONAL</span>  
 Selects which part(s) of the foot traffic data will be returned. Can be `limited`, `day`, or `both`. Default is `limited`. With `limited` selected, only the foot traffic data between the selected hours (`hour_min` and `hour_max`) is returned in the `day_raw` value result (or whole day when no hours are selected). This also applies when combining with `now` or `live` in the input. When `day` is selected, foot traffic data for the whole day is returned (regardless of the filtered hours) in the `day_raw_whole` value result. The `day_raw` value is in this case not returned. When `both` is selected, both the previously described `day_raw` and `day_raw_whole` value results are returned in the response.   
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
 Sets the time and day filter to the current day and hour in local time. Note: This option only takes into account one timezone! So it is best to use this parameter only when requesting venues within one timezone. When a collection_id is given, the timezone of the first venue in the collection is chosen. When bounding box parameters are given, the timezone of the center of the box is chosen as the timezone. When `lat`, `lng` are given the timezone of the given coordinate is chosen. When no geographic parameters are given the timezone is based on the first venue in your account. So if the determined timezone indicates currently 2 PM, the foot traffic forecast for all venues - regardless of the individual venue timezones - will be for 2 PM. Cannot be used in combination with the `live`, `day_int`, `hour_min`, and `hour_max` parameters.  
 &nbsp; 
- **live** `bool` <span style="color:blue">OPTIONAL</span>  
 Will display the live foot traffic data. Venues without live data will be filtered out. The local time of the first venue is taken that matches the filter criteria. By default the live data is not refreshed, see parameter `live_refresh`. Cannot be used in combination with the `now`, `day_int`, `hour_min`, and `hour_max` parameters. Warning: When using `live_refresh=true` the limit is only applied after refreshing (new venue foot traffic forecast) all matching venues individually. This can therefore result in high API credit usage eventhough a limit is set.
 &nbsp; 
- **live_refresh** `bool` <span style="color:blue">OPTIONAL</span>
 Live_refresh set to `true` will refresh all live and forecast data (new venue Foot Traffic Forecast) for each individual venue meeting the filter. This will slow down the request and results in extra API credits per refreshed venue. By default set to `false` to get a faster response and lower API credit usage. Note: The live_refresh will ignore the `limit` parameter to refresh all venues matching the other parameters. Only after the refresh the venue limit is applied. This may result in high API credit usage. Use the New Forecast or Live endpoints to manually control which venues needs to be updated.
 &nbsp; 
- **types** `list` <span style="color:blue">OPTIONAL</span>  
 Filters on one or more venue types. All types are selected if the `types` parameter is omitted. Possible types are (most common shown first) `RESTAURANT, SHOPPING, FAST_FOOD, BAR, SUPERMARKET, GROCERY, PARK, OTHER, APPAREL, FOOD_AND_DRINK, CAFE, SHOPPING_CENTER, COFFEE, AIRPORT, SPORTS_COMPLEX, PHARMACY, PERSONAL_CARE, VEHICLE, GAS_STATION, MUSEUM, DENTIST, LIBRARY, BANKING, TOURIST_DESTINATION, CASH_MACHINE, FOOD_DELIVERY, EVENT_VENUE, SPA, MARKET, CLUBS, PUBLIC_TRANSIT, BREWERY, SPORTING_GOODS, HISTORICAL, PERFORMING_ARTS, DOCTOR, AMUSEMENT_PARK, GIFTS, TEA, CHURCH, SKILL_INSTRUCTION, TRAIN_STATION, ARTS, GOLF, ZOO, BOTANICAL_GARDEN, NATIONAL_PARK, SUBWAY_STATION, CASINO, MOVIE_THEATER, POST_OFFICE, HIKING, GOLF_COURSE, NATURE_RESERVE, BRIDGE, BUS_STATION, GOVERNMENT, REST_AREA, WINERY, SCENIC_POINT, SOUVENIR_SHOP, CITY_HALL, BOATING, CONCERT_HALL, SWIMMING, MONUMENT, SOCCER, CAR_RENTAL, MOSQUE, INDUSTRIAL, VISITOR_CENTER, ANTIQUES, AQUARIUM, PALACE, HINDU_TEMPLE, STADIUM, WINTER_SPORTS, BUDDHIST_TEMPLE, EMBASSY, TEMPLE, TENNIS, BASEBALL, FERRY_TERMINAL, FISHING, POLICE, SCHOOL, BAKERY, AGRICULTURE, CRICKET, FAIRGROUNDS, GONDOLA_LIFT_STATION, HOSPITAL, LIGHTHOUSE, MILITARY, MORMON_TEMPLE, UNIVERSITY`  
 &nbsp; 
- **lat** `float` <span style="color:blue">OPTIONAL</span>  
   Geographic latitude of the search circle. `lat` must be combined with `lng`, and `radius`. The search circle cannot be combined with the bounding box parameters. A maximum of 3 decimal floating points are allowed (≈ 111 meter). This will be enforced starting from September 1st, 2021.  Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp;
- **lng** `float` <span style="color:blue">OPTIONAL</span>  
   Geographic longitude of the search circle.  `lng` must be combined with `lat`, and `radius`. The search circle cannot be combined with the bounding box parameters. A maximum of 3 decimal floating points are allowed (≈ 111 meter). This will be enforced starting from September 1st, 2021.  Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp; 
- **radius** `int` <span style="color:blue">OPTIONAL</span>  
   Radius of the search circle in meter.  `radius` must be combined with `lat`, and `lng`. The search circle cannot be combined with the bounding box parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp; 
- **lat_min** `float` <span style="color:blue">OPTIONAL</span>  
   Minimum latitude of the bounding box (South-West). A maximum of 3 decimal floating points are allowed (≈ 111 meter). This will be enforced starting from September 1st, 2021. `lat_min` must be combined with `lat_max`, `lng_min` and `lng_max`. The bounding box cannot be combined with the circle parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required. 
  &nbsp; 
- **lng_min** `float` <span style="color:blue">OPTIONAL</span>  
   Minimum longitude of the bounding box (South-West). A maximum of 3 decimal floating points are allowed (≈ 111 meter). This will be enforced starting from September 1st, 2021.  `lng_min` must be combined with `lng_max`, `lat_min` and `lat_max`. The bounding box cannot be combined with the circle parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp; 
- **lat_max** `float` <span style="color:blue">OPTIONAL</span>  
   Maximum latitude of the bounding box (North-East). A maximum of 3 decimal floating points are allowed (≈ 111 meter). This will be enforced starting from September 1st, 2021.  `lat_max` must be combined with `lat_min`, `lng_min` and `lng_max`. The bounding box cannot be combined with the circle parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp; 
- **lng_max** `float` <span style="color:blue">OPTIONAL</span>  
   Maximum longitude of the bounding box (North-East). A maximum of 3 decimal floating points are allowed (≈ 111 meter). This will be enforced starting from September 1st, 2021.  `lng_max` must be combined with `lng_min`, `lat_min` and `lat_max`. The bounding box cannot be combined with the circle parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp; 
- **price_min** `int` <span style="color:blue">OPTIONAL</span>  
   Minimum price level for a venue. Range `1` to `5`. Not all venues have a price level, indicated as `0`. Using `price_min` WILL filter out all venues without a price level.  
  &nbsp; 
- **price_max** `int` <span style="color:blue">OPTIONAL</span>  
   Maximum price level for a venue. Range `1` to `5`. Not all venues have a price level, indicated as `0`. Using `price_max` will NOT filter out all venues without a price level.  
  &nbsp; 
- **rating_min** `float` <span style="color:blue">OPTIONAL</span>  
   Minimum rating for a venue. Possible values are `2.0, 2.5, 3.0, 3.5, 4.0, 4.5`. Venues without a rating (0) will NOT be returned when applying this filter.  
  &nbsp; 
- **rating_max** `float` <span style="color:blue">OPTIONAL</span>  
   Maximum rating for a venue. Possible values are `2.0, 3.0, 3.5, 4.0, 4.5, 5.0`. Venues without a rating (0) WILL be returned when applying this filter.
  &nbsp; 
- **reviews_min** `int` <span style="color:blue">OPTIONAL</span>  
   Minimum number of reviews for a venue. Minimum value `0`.  
  &nbsp;  
- **reviews_max** `int` <span style="color:blue">OPTIONAL</span>     
   Maximum number of reviews for a venue. Minimum value `0`.  
  &nbsp; 
- **day_rank_min** `int` <span style="color:blue">OPTIONAL</span>  
   Minimum day rank value. Ranges from day `1` to `7`, wherein `1` is the most busy ranked day of the week and `7` the least busy day of the week. Rank is based on peak values (`day_max`) of each week day. E.g. setting the value to `2` will return only the 5 least busy days.  
  &nbsp;  
- **day_rank_max** `int` <span style="color:blue">OPTIONAL</span>     
    Maximum day rank value. Ranges from day `1` to `7`, wherein `1` is the most busy ranked day of the week and `7` the least busy day of the week. Rank is based on peak values (`day_max`) of each week day. E.g. setting the value to `2` will return only the 1st and 2nd most busy days.  
  &nbsp; 
- **order_by** `int` <span style="color:blue">OPTIONAL</span>
   BETA: Sort venues on foot traffic intensity data. Order venues by a specific parameter. Can be `reviews`,`rating`,`price_level`,`live`,`now`,`name`,`day_rank_max`,`day_rank_mean`,`day_max`,`day_mean`,`date`, `dwell_time_min`,`dwell_time_max`,`0`,`1`,`2`,`3`,`4`,`5`,`6`,`7`,`8`,`9`,`10`,`11`,`12`,`13`,`13`,`14`,`15`,`16`,`17`,`18`,`19`,`20`,`21`,`22`,`23`. Default is `reviews`. Max two comma separated parameters allowed (e.g. `order_by=rating,reviews`). The 24 numbers represent the foot traffic data for each of the 24 hours in a day. E.g. `16` will sort the venues based on predicted foot traffic at 16:00 (4PM). Warning: Venues forecasted before July 1st, 2021 need to be updated (new foot traffic forecast) to order them correctly.  
  &nbsp; 
- **order** `int` <span style="color:blue">OPTIONAL</span>
   Order the `order_by` parameters ascending or descending. Can be `asc` or `desc`.  Default `desc`. Max two comma seperated parameters allowed (e.g. `order=desc,asc`).  
  &nbsp; 
- **limit** `int` <span style="color:blue">OPTIONAL</span>    
   Maximum number returned venues. Default `5000`, min `0`, max `10000`. Higher limits result in slower responses and higher API credit usage. Warning: When using `live_refresh=true` the limit is only applied after refreshing (new venue foot traffic forecast) all matching venues individually. This can therefore result in high API credit usage eventhough a limit is set.
  &nbsp; 
- **page** `int` <span style="color:blue">OPTIONAL</span>    
   Selects the page number. Default page `0`. Min page `0`.  
  &nbsp; 


<aside class="notice">
Query filtered venues endpoint: https://besttime.app/api/v1/venues/filter
</aside>

<aside class="notice">
HTTP method: GET
</aside>

<aside class="warning">
API Credit usage per API call for this endpoint depends on the number of returned venues and your plan. See 'API key credits' for more information.
</aside>

<aside class="warning">
The Venue Filter endpoint is by default limited to 30 requests per minute. Contact us for higher limits.
</aside>



> The above request returns a JSON response like this (this example only contains a list with one venue):

```json
{
  "status": "OK", 
  "venues": [
    {
      "day_int": 0, 
      "day_raw": [
        85,
        60,
        30,
        10,
        0,
        0
      ], 
      "day_raw_whole": [
        0,
        0,
        0,
        0,
        10,
        15,
        15,
        15,
        20,
        25,
        45,
        70,
        85,
        60,
        30,
        10,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ], 
      "venue_address": "61 Piccadilly Mayfair, London W1J 0DY United Kingdom", 
      "venue_id": "ven_386d55494f76464873784752676b6445593949455752594a496843", 
      "venue_lat": 51.5079836, 
      "venue_lng": -0.1404946, 
      "venue_name": "Caffe Concerto Green Park",
      "venue_type": "CAFE",
      "venue_dwell_time_min": 30,
      "venue_dwell_time_max": 70,
      "price_level": 2,
      "rating": 4.8,
      "reviews": 1276,
    }, 
    {
      "day_int": 0, 
      "day_raw": [
        75,
        95,
        95,
        70,
        0,
        0
      ],
      "day_raw_whole": [
        0,
        0,
        15,
        25,
        35,
        40,
        45,
        45,
        40,
        35,
        40,
        55,
        75,
        95,
        95,
        70,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "venue_address": "14 Riding House St Fitzrovia, London W1W 7HR United Kingdom", 
      "venue_id": "ven_6372542d36476a4a59686d52676b646155646e713661514a496843", 
      "venue_lat": 51.5183082, 
      "venue_lng": -0.1415526, 
      "venue_name": "The Great Thai Restaurant",
      "venue_type": "RESTAURANT",
      "venue_dwell_time_min": 40,
      "venue_dwell_time_max": 80,
      "price_level": 3,
      "rating": 4.1,
      "reviews": 4276,
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
    List of raw foot traffic data values for each hour of the day, or within the selected hour range. The list contains percentages ranging from `0` to `100`. Indicating the relative foot traffic percentage. Percentages are based on historical visits for the given hour, relative to the biggest peak of the week for this venue. When the `now` or `live` parameter is `true` the list will contain one `int` for the current hour in the local time. `day_raw` is returned when input parameter `foot_traffic` is set to `limited` or `both`. 
    &nbsp;
  - venues[N].**day_raw_whole** `list`  
  List of foot traffic data values for the whole day - regardless if a filter is applied on specific hours. The list contains percentages ranging from `0` to `100`. Indicating the busyness percentage. Percentages are based on historical visits for the given hour, relative to the biggest peak of the week for this venue. `day_raw` is returned when input parameter `foot_traffic` is set to `day` or `both`. By default this value is not returned.
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
 - venue_info.**venue_type** `string`  
   Type of venue, or `OTHER` when not available. Possible types are (most common shown first) `RESTAURANT, SHOPPING, FAST_FOOD, BAR, SUPERMARKET, GROCERY, PARK, OTHER, APPAREL, FOOD_AND_DRINK, CAFE, SHOPPING_CENTER, COFFEE, AIRPORT, SPORTS_COMPLEX, PHARMACY, PERSONAL_CARE, VEHICLE, GAS_STATION, MUSEUM, DENTIST, LIBRARY, BANKING, TOURIST_DESTINATION, CASH_MACHINE, FOOD_DELIVERY, EVENT_VENUE, SPA, MARKET, CLUBS, PUBLIC_TRANSIT, BREWERY, SPORTING_GOODS, HISTORICAL, PERFORMING_ARTS, DOCTOR, AMUSEMENT_PARK, GIFTS, TEA, CHURCH, SKILL_INSTRUCTION, TRAIN_STATION, ARTS, GOLF, ZOO, BOTANICAL_GARDEN, NATIONAL_PARK, SUBWAY_STATION, CASINO, MOVIE_THEATER, POST_OFFICE, HIKING, GOLF_COURSE, NATURE_RESERVE, BRIDGE, BUS_STATION, GOVERNMENT, REST_AREA, WINERY, SCENIC_POINT, SOUVENIR_SHOP, CITY_HALL, BOATING, CONCERT_HALL, SWIMMING, MONUMENT, SOCCER, CAR_RENTAL, MOSQUE, INDUSTRIAL, VISITOR_CENTER, ANTIQUES, AQUARIUM, PALACE, HINDU_TEMPLE, STADIUM, WINTER_SPORTS, BUDDHIST_TEMPLE, EMBASSY, TEMPLE, TENNIS, BASEBALL, FERRY_TERMINAL, FISHING, POLICE, SCHOOL, BAKERY, AGRICULTURE, CRICKET, FAIRGROUNDS, GONDOLA_LIFT_STATION, HOSPITAL, LIGHTHOUSE, MILITARY, MORMON_TEMPLE, UNIVERSITY`   
  &nbsp;
  - venues[N].**venue_dwell_time_min** `int`  
   Minimum usual visitor dwell time in minutes, or `0` when not available.  
  &nbsp;
  - venues[N].**venue_dwell_time_max** `int`  
   Maximum usual visitor dwell time in minutes, or `0` when not available.   
  &nbsp;
  - venues[N].**price_level** `int`
   Price level for a venue. Range `1` (cheapest) to `5` (most expensive. Not all venues have a price level, indicated with `null`. 
  &nbsp; 
  - venues[N].**rating** `float`
   Rating for a venue. Ranging from `1.0` to `5.0`. Not all venues have a rating, indicated with `0`. 
  &nbsp; 
  - venues[N]**reviews** `int`   
  Number of reviews for a venue. Minimum value `0`. Not all venues have a number of reviews, indicated as `0`.   
  &nbsp; 
- **status** `string` 
 Status of the response. Either `OK` or `error`.
