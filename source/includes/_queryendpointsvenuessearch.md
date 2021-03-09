## Venue Search (COMING SOON)

> Find and add new venues based on a search query.

```python
import requests
import json

url = "https://besttime.app/api/v1/venues/search"

params = {
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
    'q': 'quiet supermarkets in sydney australia sunday morning',
    'num': 100,
    'fast': False,
    'opened': 'now'
}

response = requests.request("POST", url, params=params)

data = json.loads(response.text)

print(data)
```

```shell
# cURL
curl --location --request POST 'https://besttime.app/api/v1/venues/search?api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&q=quiet%20supermarkets%20in%20sydney%20australia%20sunday%20morning&num=100&fast=false&opened=now'
```

```javascript
var params = {
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
    'q': 'quiet supermarkets in sydney australia sunday morning',
    'num': 100,
    'fast': false,
    'opened': 'now'
}

$.ajax({
"url": "https://besttime.app/api/v1/venues/search?" + new URLSearchParams(params),
"method": "POST"
}).done(function (response) {
    console.log(response);
});
```


### Input attributes Venue Search

Find and add new venues based on a search query. The search query can e.g. contain the name of a venue (e.g. McDonald's, Walmart,etc), or a type of venue (e.g. supermarkets, pizza, beach, things to do, etc). 

The search query can be narrowed down with additional filters like the location (e.g. a neighborhood, city, or country), or add geographical data (lat, lng, radius) to find venues related to the search query in a geographic location.

Multiple API endpoints are involved from entering a search input until returning foot-traffic data for the found venues venues.
The Venue Search model will lookup venues in the background and will forecast them subsequently. The endpoint will reply with a background task `job_id`, and a `collection_id`.  You can poll the Venue Search Result endpoint to poll the result progress. Once the TODO!!!

#### Venue filters

The venue search endpoint will return a link to view the results in the 'Radar tool' and the 'venue filter' endpoint. The venue search endpoint accepts filters similar to the 'venue filter' endpoint and Radar tool. By providing these parameters the links to the Radar tool and Venue Filter endpoint will automatically include the filter parameters. 

#### Natural langauge in the search query as filters

Besides seperate parameters as filter inputs, the `q` search query understands also a variaty of natural language that will be translated into the related filter parameters. You can use it to filter on busyness, day of week, day part, or time range. For example:

Busyness natural language examples:
- Search query `Busy bars in Sydney Australia` will result in a search for `bars in Sydney Australia` and will set the filter parameter minimum busyness to 50% `busy_min=50`. 
- Search query `Quiet supermarkets in Los Angeles, CA` will result in a search for `supermarkets in Los Angeles, CA` and will set the filter parameter maximum busyness to 50% `busy_max=50`.
- Search query `10% to 60% busy shops in New York City` will result in a search for `shops in New York City` with `busy_min=10` and `busy_max=60` as filter parameters.

Strings that will trigger the busyness filters are: 
`busy` -> `busy_min=50`,
`quiet`-> `busy_max=50`,
Define a range with multiple percentages including the word `busy`:
E.g. `40% to 90% busy bars in New York City`.
Define a custom minimum or maximum using the strings:
- `min`,`minimal`, `minimum`,`least`
- `max`,`maximal`,`maximum`,`most`
E.g. `at least 60% busy bars in Melbourne Australia` will set the filter to `busy_min=60`


Day of week  natural language examples:
- Search query `shopping malls in Singapore on Monday` will result in a search for `shopping malls 
in Singapore` and with `day_int=0` as filter parameters.
- Search query `bars in Melbourne Australia Friday` will result in a search for `bars in Melbourne Australia` with `day_int=4` as filter parameter.

Strings (case insensitive) that will trigger the day of week are :
- `Monday` -> `day_int=0`,  
- `Tuesday` -> `day_int=1`,  
- `Wednesday`  -> `day_int=2`,  
- `Thursday` -> `day_int=3`,  
- `Friday` -> `day_int=4`,  
- `Saturday` -> `day_int=5`,  
- `Sunday` -> `day_int=6`

Time of day natural language examples:
- Search query `quiet shopping malls in Singapore this morning` will result in a search for `shopping malls in Singapore` and with `busy_max=50`, `hour_min=6`, and `hour_max=11` as filter parameters.
- Search query `busy bars in Melbourne Australia Saturday evening` will result in a search for `bars in Melbourne Australia` and with `busy_min=50`, `hour_min=18`, and `hour_max=0` as filter parameters.
- Search query `min 60% busy bars in Melbourne Australia Saturday after 9PM` will result in a search for `bars in Melbourne Australia` and with `busy_min=60`, `day_int=5`,`hour_min=21` as filter parameters.
- Search query `max 40% busy restaurants in Melbourne Australia on Wednesday from 13 until 15` will result in a search for `restaurants in Melbourne Australia` and with `busy_max=40`, `day_int=2`, `hour_min=13`, and `hour_max=15` as filter parameters.

Strings (case insensitive) that will trigger the time of day filters:
- Dayparts (only works in combination with a day of the week string like e.g. `Monday`, or `this`):  
  `morning` -> `hour_min=6`, `hour_max=11`,  
  `afternoon` -> `hour_min=12`, `hour_max=17`,  
  `evening` -> `hour_min=18`, `hour_max=0`,  
  `night` -> `hour_min=21`, `hour_max=5`,  
- Min and/or max time in combination with a 12 or 24 hour notation:  
  `after`, `before`, `until`, `till`, `from`  
  e.g. `until 1pm` or `from 9 till 15`
- `now` sets the the `hour_min` and `hour_max` value to filter foot-traffic data on current hour local time of the first venue. E.g. `busy bars in Sydney Australia now`. `Now` cannot be used in combination with day and other time triggers.
- `live` will only show venues with real-time live data. `live` cannot be used in combination with day and other time triggers.


This query endpoint requires the private API key. 

- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. The endpoint will only return venues that are forecasted with this private API key. See [API keys](#api-keys) for more info.
 &nbsp;
 - **q** `string` <span style="color:orange">REQUIRED</span>  
 Text query to search venues with a matching venue name (e.g. Whole Foods), or venue type (e.g. restaurants), and location (e.g. neighborhood, city, state or country). You can use natural language to automatically add venue filters, see TODO fix link [Natural langauge in the search query as filters](#Natural langauge in the search query as filters).
 &nbsp;
- **num** `int` <span style="color:blue">OPTIONAL</span>  
Maximum number of search results, with increments of 20 venues, and a range from `20` to `200`.
Default number is `20`. API credits for this endpoint are counted per `20` search results. The search time grows liniarly with the amount of requested numbers (see also parameter `fast`).
&nbsp;
- **opened** `string` <span style="color:blue">OPTIONAL</span>  
Search for venues with specific opening times. Options are `24`, `now`, `all` . `24` will return venues with a 24 hour opening time. `now` will return venues that are opened at this moment. `all` will return all venues regardless of their opening hours. Defaults to `all`.
 &nbsp;
- **fast** `boolean` <span style="color:blue">OPTIONAL</span>  
Boolean to select the normal speed or fast search method. Searching with the fast method is charged with more API credits. Defaults to `true` (fast search speed). The fast method is limited to a maximum `num` of `60`. Selecting a higher number will automatically use the normal speed method. Select `false` to save on API credits or to search for more venues. See API Credits for more info TODO add Credits link. Fixed packages and Metered Pro each have limited amount of fast search queries per month. Contact us for high volume fast search queries.
 &nbsp;

- **collection_id** `string` <span style="color:blue">OPTIONAL</span>  
Add the results to an existing or user-defined collection_id. If this parameter is omitted a new unique collection_id will be generated. All successfully forecasted venues will be automatically added to this collection. By giving an existing collection_id the user can merge the new venues with an existing venue collection. See [Collections](#collections) for more info.
 &nbsp;

<aside class="warning">
The 'venue search' endpoint accepts also the filters below, similar to the `venue filter` filter parameters. These 'venue filter' parameters are NOT applied on the initial 'search venue' venue results, but are only passed on to the 'venue filter' and 'radar' URL links. When a 'venue search' is performend with filters set to e.g. `busy_min=60` the 'venue search` results will include and forecast all found venues. Only the subsequent 'venue filter'/ 'radar tool' step applies the filters. 
</aside>  
&nbsp;


- **busy_min** `int` <span style="color:blue">OPTIONAL</span>  
Minimum busyness for the filtered venues, ranging from `0` to `100` procent.  Use `busy_conf` parameter to change the filter method.  
 &nbsp;
- **busy_max** `int` <span style="color:blue">OPTIONAL</span>  
Maximum busyness for the filtered venues, ranging from `0` to `100` procent. Use `busy_conf` parameter to change the filter method.    
 &nbsp;
- **busy_conf** `string` <span style="color:blue">OPTIONAL</span>  
Selects how `busy_min` and `busy_max` filters on busyness percentage. Possible options are `any` or `all`. Defaults to  `any`. `any` will return venues when at least one of the (selected) hours matches the `busy_min` and/or `busy_max` filter(s). `all` will return venues when all (selected) hours match the `busy_min` and/or `busy_max` filter(s). Use the `hour_min` and/or `hour_max` parameters to select specific hours were the `busy_min` and/or `busy_max` filters are applied on.  
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
- **live_refresh** `bool` <span style="color:blue">OPTIONAL</span> <span style="color:green"> New</span>     
 Live refresh set to `true` will refresh all live and forecast data for each individual venue meeting the filter.  This will slow down the request and results in extra API credits per refreshed venue. 
 &nbsp; 
- **collection_id** `string` <span style="color:blue">OPTIONAL</span> <span style="color:green"> New</span>     
 Returns only venues added to given collection. See Collections for more info. TODO add link to collection info
 &nbsp; 
- **types** `list` <span style="color:blue">OPTIONAL</span>  
 Filters on one or more venue types. All types are selected if the `types` parameter is ommited. Possible types are `['APPAREL', 'ARTS', 'BANKING', 'BAR', 'BOTANICAL_GARDEN', 'CAFE', 'CAR_RENTAL', 'CHURCH', 'CITY_HALL', 'COFFEE', 'DENTIST', 'DOCTOR', 'EMBASSY', 'EVENT_VENUE', 'FAST_FOOD', 'FOOD_AND_DRINK', 'FOOD_DELIVERY', 'GAS_STATION', 'GOVERNMENT', 'GROCERY', 'LODGING','MARKET', 'MOVIE_THEATER', 'MUSEUM', 'Other', 'PARK', 'PERFORMING_ARTS', 'PERSONAL_CARE', 'PHARMACY', 'PUBLIC_TRANSIT', 'RESTAURANT', 'SCHOOL', 'SHOPPING', 'SKILL_INSTRUCTION', 'SPA', 'SPORTS_COMPLEX', 'SUPERMARKET', 'TEA', 'TOURIST_DESTINATION', 'VISITOR_CENTER']`  
 &nbsp; 
- **lat** `float` <span style="color:blue">OPTIONAL</span>  
   Geographic latitude of the search circle. `lat` must be combined with `lng`, and `radius`. The search circle cannot be combined with the bounding box parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp;
- **lng** `float` <span style="color:blue">OPTIONAL</span>  
   Geographic longitude of the search circle.  `lng` must be combined with `lat`, and `radius`. The search circle cannot be combined with the bounding box parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp; 
- **radius** `int` <span style="color:blue">OPTIONAL</span>  
   Radius of the search circle in meter.  `radius` must be combined with `lat`, and `lng`. The search circle cannot be combined with the bounding box parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp; 
- **lat_min** `float` <span style="color:blue">OPTIONAL</span>  
   Minimum latitude of the bounding box (South-West). `lat_min` must be combined with `lat_max`, `lng_min` and `lng_max`. The bounding box cannot be combined with the circle parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp; 
- **lng_min** `float` <span style="color:blue">OPTIONAL</span>  
   Minimum longitude of the bounding box (South-West). `lng_min` must be combined with `lng_max`, `lat_min` and `lat_max`. The bounding box cannot be combined with the circle parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp; 
- **lat_max** `float` <span style="color:blue">OPTIONAL</span>  
   Maximum latitude of the bounding box (North-East). `lat_max` must be combined with `lat_min`, `lng_min` and `lng_max`. The bounding box cannot be combined with the circle parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp; 
- **lng_max** `float` <span style="color:blue">OPTIONAL</span>  
   Maximum longitude of the bounding box (North-East). `lng_max` must be combined with `lng_min`, `lat_min` and `lat_max`. The bounding box cannot be combined with the circle parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp; 
- **price_min** `int` <span style="color:blue">OPTIONAL</span><span style="color:green"> New</span>  
   Minimum price level for a venue. Range `1` to `5`. Not all venues have a price level. Using `price_min` filters out all venues without a price level.  
  &nbsp; 
- **price_max** `int` <span style="color:blue">OPTIONAL</span><span style="color:green"> New</span>    
   Maximum price level for a venue. Range `1` to `5`. Not all venues have a price level. Using `price_max` filters out all venues without a price level.  
  &nbsp; 
- **rating_min** `float` <span style="color:blue">OPTIONAL</span><span style="color:green"> New</span>    
   Minimum rating for a venue. Possible values are `2.0, 2.5, 3.0, 3.5, 4.0, 4.5`.  
  &nbsp; 
- **rating_max** `float` <span style="color:blue">OPTIONAL</span><span style="color:green"> New</span>    
   Maximum rating for a venue. Possible values are `2.0, 3.0, 3.5, 4.0, 4.5, 5.0`.  
  &nbsp; 
- **reviews_min** `int` <span style="color:blue">OPTIONAL</span><span style="color:green"> New</span>    
   Minimum amount of reviews for a venue. Minimum value `0`.  
  &nbsp;  
- **reviews_max** `int` <span style="color:blue">OPTIONAL</span> <span style="color:green"> New</span>   
   Maximum amount of reviews for a venue. Minimum value `0`.
  &nbsp; 


<aside class="notice">
Search venue endpoint: https://besttime.app/api/v1/venues/search
</aside>

<aside class="notice">
HTTP method: POST
</aside>

<aside class="warning">
API Credit usage per API call for this endpoint depends on the number `num` of requested venues. See 'API key credits' for more information.
</aside>


> The above request returns a JSON response with links to the background job:

```json
{
    "_links": {
        "venue_forecast_progress": "https://besttime.app/api/v1/venues/progress?job_id=e0880f28-3a19-4871-a355-4ca21f10c2c8&collection_id=col_ac734e76ad2d4696a5a66541c67587e8"
    },
    "collection_id": "col_ac734e76ad2d4696a5a66541c67587e8",
    "job_id": "e0880f28-3a19-4871-a355-4ca21f10c2c8",
    "status": "OK"
}
```


### Response attributes Query Venues
The JSON response will contain a `list` with venue `objects`.

- **_links** `object` 
 Each venue object contains venue information and busyness data.  
  &nbsp;
  - _links.**venue_forecast_progress** `string`  
    Link to the background job. Use this link to check the progress on the search venues result. When the job is finished it will display the found venues, how many venues include forecast/ live data, and links to show the found venues with foot-traffic results in the 'Radar tool` and 'venue filter' endpoint. For more info see venue_forecast_progress TODO link.
    &nbsp;
    
    &nbsp;
- **collection_id** `string` 
 TODO
 - **job_id** `string` 
 TODO
- **status** `string` 
 Status of the response. Either `OK` or `error`.
