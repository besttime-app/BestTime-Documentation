

<!-- Content from _apireference.md -->


# API Reference

The API Reference explains how:

- authentication works using the API Keys.
- credits are handled with your API usage.
- to create a new venue forecast.
- to query an existing forecast to get specific, or more detailed data.

<a name="api-keys"></a> 
## API Key 


BestTime.app uses API keys to allow access to the API. You can find or generate API keys at the [API keys Management](http://besttime.app/api/v1/api_keys_list) page.

BestTime.app expects for the API key to be included in all API requests to the server.

Authentication for the API is done using API keys.
There are two types of API keys; Private keys are used to create a new forecast, and public keys to query data from existing forecasted venues. The private key can be used to create, delete and list forecasts. As the name suggests, the private key should be kept secret, to avoid other people from forecasting new venues and abusing your limited forecast credits. The public key can be used to query existing venue forecasts. However, it can only be used to get existing forecast data (read-only). 

API keys are generated in pairs, and you can generate multiple API key sets (pairs) in the API key management page. When using multiple API keys, you should remember that you can only query forecasts from the same key set. 

All key set use credits from the same account. When an API key is compromised, you can delete the API key set through the API Key management page.

<b>Highly recommended to read first:
- [BestTime tools beginners tutorial](https://blog.besttime.app/foot-traffic-nightlife-bars/)
- [BestTime Software API beginners tutorial](https://blog.besttime.app/beginners-guide-foot-traffic-data-software-api/)
</b>  

## Authentication

> To authorize, use this code:


```python
import requests

url = "https://besttime.app/api/v1/keys/pri_a00de9e302662c0217a9cf08ab304122"

response = requests.request("GET", url)

print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/keys/pri_a00de9e302662c0217a9cf08ab304122'
```

```javascript

fetch(`https://besttime.app/api/v1/keys/pri_a00de9e302662c0217a9cf08ab304122`, {
  method: 'GET'
}).then(function(data) { console.log(data); });
```

You can find or generate API keys at the [API keys Management](http://besttime.app/api/v1/api_keys_list) page.

> The above command returns JSON structured like this:

```json
  {
    "active": true,
    "api_key_private": "pri_a00de9e302662c0217a9cf08ab304122",
    "api_key_public": "pub_e11661721b084d36b8f469a2c012e754",
    "status": "OK",
    "valid": true
  }
```

### Private and public API keys

- **api_key_private** `string`  
 32 Character private API key. Used to create new forecasts or get live data.  
 &nbsp; 
- **api_key_public** `string`  
 32 Character public API key. Used to query (lookup) specific data from an excisting forecast.  
 &nbsp;  

<aside class="notice">
Base endpoint: https://besttime.app/api/v1/keys
</aside>

<aside class="notice">
HTTP method: GET
</aside>


<aside class="notice">
Make sure to replace <code>pri_a00de9e302662c0217a9cf08ab304122</code> with your 36 char private API key.
</aside>


## Credits

For metered API subscription API credits are used to calculate your total monthly bill. See the pricing page for the price per API credit. 

The number of credits per API call depends on the used API endpoint. The tools on the website also use the API internally and will therefore also count towards your total API usage.

Alternatively, you can buy a Package subscription. Then you always pay a fixed fee per month and can call the API as many times as you want (see the BestTime pricing page for more details on the packages).

 
&nbsp;  

| API Endpoint                           | Credits     | API Key required |
|------------------------------------|------------------|------------------|
| New foot traffic forecasts (success)             | 2          | Private          | 
| New foot traffic forecasts (unsuccessful)        | 1         | Private        |
| Live foot traffic data                           | 1         | Private          | 
| Venue (all/ filter/ update)           | 1 / 10 venues | Private          |
| Venue Search (Normal)          | 1 / 20 venues | Private          |
| Venue Search (Fast)          | 5 / 20 venues | Private          |
| Query (existing forecast)                | 1         | Public            |  
 
 &nbsp; 

Unsuccessful forecasts are also counted as credits, with the exception of server errors. This is to prevent overloading the API servers with low quality address inputs.

It is the users responsibility to prevent api key abuse. Hide your API keys secure to prevent other people from using API credits resulting in higher monthly subscription fees.

The Venue Search functionality counts credits for finding matching venues, but this result does not include foot-traffic data. Therefore, the Venue Search function will automatically pushes the found venues to the 'New foot-traffic forecast' API endpoint. A 'normal' speed Venue search for max 20 venues will therefore cost: 1 Venue search normal credit + 20 * 2 New Forecast (successful) credit = 41 credits (equals to approximately $0.32 with the Premium plan). This is the maximum number of credits used. If the search result includes less venues, or if a venue does not have foot-traffic data the number will be lower. In a future version we will give the user the possibility to decide to not automatically forecast all found venues through the Venue Search tool. 


### Subscription plans
BestTime has two types of plans. Metered and packaged plans. The metered plans will automatically charge you depending on the credit usage at the end of a (monthly) billing cycle. The basic plan is the lowest-priced plan. All functionality is available in the basic plan, 

BestTime also offers multiple 'packaged' plans if you don't like the uncertainty of a metered plan. The packaged plans have a fixed price per month and unlimited forecast, live, query and venue API calls. However, each package plan is limited to a certain number of new venues-, and venue search calls per calender month.


## HTTP (Error) API codes

BestTime uses the following HTTP codes

| Code  | Meaning   | 
|---------------|-------------|
| 200              | OK      | 
| 400             | Bad Request - check your API parameters |
|401               | Unauthorized |
| 404              | Not found - API resource not found |
| 405               | Method Not Allowed - You tried to access the API with an invalid route |
|429 |Too Many Requests - You have been rate-limited
|500 | Internal Server Error - We have a problem with the server and the team has been automatically notified
| 503 | Service Unavailable

&nbsp;  

By default the API is limited to 300 API requests per minute. The Venue Search API endpoint is limited to 30 request per minute and 300 requests per hour. The Venue Filter is limited to 30 request per minute. You will receive a HTTP 429 'too many requests' above this threshold. Contact us for if you need higher limits.

<!-- Content from _examples.md -->

# Examples

## Foot traffic forecast + Live chart (HTML / Javascript)
<a href="https://github.com/besttime-app/examples/blob/main/besttime-forecast-live-today-echarts.html">See example on Github</a>

<img src="https://raw.githubusercontent.com/besttime-app/examples/main/forecast-day.jpg">


## Foot traffic Week heatmap (HTML / Javascript)

<a href="https://github.com/besttime-app/examples/blob/main/besttime-forecast-weekheat-apex.html">See example on Github</a>
<img src="https://raw.githubusercontent.com/besttime-app/examples/main/forecast-week.jpg">

<!-- Content from _forecastendpoints.md -->


# New foot-traffic forecast
<a name="forecast-new-link"></a>

> Returns foot-traffic forecast for a venue based on a name and address

```python
import requests

url = "https://besttime.app/api/v1/forecasts"

params = {
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
    'venue_name': 'McDonalds',
    'venue_address': 'Ocean Ave, San Francisco'
}

response = requests.request("POST", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request POST 'https://besttime.app/api/v1/forecasts?
api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&
venue_name=McDonalds&
venue_address=Ocean%20Ave%2C%20San%20Francisco'
```

```javascript
const params = new URLSearchParams({
 'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
  'venue_name': 'McDonalds',
  'venue_address': 'Ocean Ave, San Francisco'
});

fetch(`https://besttime.app/api/v1/forecasts?${params}`, {
  method: 'POST'
}).then(function(data) {
  console.log(data);
});
```

> The above request returns JSON structured like this:

```json
  {
    "analysis": [
        {
            "day_info": {
                "day_int": 0,
                "day_rank_max": 6,
                "day_rank_mean": 4,
                "day_text": "Monday",
                "venue_open_close_v2": {
                    "24h": [
                        {
                            "opens": 6,
                            "closes": 23
                        }
                    ],
                    "12h": [
                        "6am–11pm"
                    ]
                },
            },
            "day_raw": [
                10,
                25,
                40,
                55,
                65,
                75,
                75,
                75,
                75,
                75,
                70,
                65,
                50,
                40,
                30,
                25,
                25,
                25,
                20,
                15,
                10,
                0,
                5,
                5
            ],
            "hour_analysis": [
                {
                    "hour": 6,
                    "intensity_nr": -1,
                    "intensity_txt": "Below average"
                },
                ... Other hours hidden. See full JSON example link below
            ],
            "peak_hours": [
                {
                    "peak_start": 8,
                    "peak_max": 11,
                    "peak_end": 23,
                    "peak_intensity": 4
                }
            ],
            "quiet_hours": [
                6,
                1,
                2,
                3
            ],
            "busy_hours": [
                9,
                10,
                11,
                12
            ],
            "surge_hours": {
                "most_people_come": 8,
                "most_people_leave": 22
            },
        },
        ... Other days hidden. See full JSON example link below
    ],
    "epoch_analysis": "1583314752",
    "status": "OK",
    "venue_info": {
        "venue_address": "1201 Ocean Ave San Francisco, CA 94112 United States",
        "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles",
        "venue_dwell_time_min": 20,
        "venue_dwell_time_max": 60,
        "venue_dwell_time_avg": 40,
        "venue_type": "FAST_FOOD",
        "venue_types": [
            "fast_food_restaurant",
            "breakfast_restaurant",
            "coffee_shop",
            "hamburger_restaurant",
            "restaurant",
            "sandwich_shop"
        ],
        "venue_lat": -8.6487349,
        "venue_lon": 115.13728069999999,
        "rating": 3.5,
        "reviews": 1204,
        "price_level": 1
    }
}}
```

> Click <a href="https://github.com/besttime-app/slate/blob/master/source/examples/forecast_new/forecast_new_response.json" target="_blank">here</a> for the full JSON response


The 'new foot traffic forecast' endpoint is used to create a [forecast](#forecasts) of a venue based on the most recent available data. Forecasts are created using the venue name and address as input. The response includes the forecast (including different analysis), and venue information.
The venue information includes the `venue_id`. This ID is the primary parameter to lookup previously forecasted venues, using the [query endpoints] (#query-endpoints).

<b>Highly recommended to read first:
- [BestTime tools beginners tutorial](https://blog.besttime.app/foot-traffic-nightlife-bars/)
- [BestTime Software API beginners tutorial](https://blog.besttime.app/beginners-guide-foot-traffic-data-software-api/)
- [HTML/ Javascript examples](#examples)
</b>

### Input attributes New Forecast

- **venue_name** `string` <span style="color:blue">OPTIONAL</span>
 Name of the venue (public business). Max input length `256` characters.  When then using the `venue_id` the `venue_name` and `venue_address` can be omitted.
 &nbsp;
- **venue_address** `string` <span style="color:blue">OPTIONAL</span>
 Address of the venue (public business). The address does not have to be exact, but needs to be precise enough for the geocoder engine to find the correct venue. The more specific the address the higher chance the geocoder will find the venue. Max input length `1024` characters. The response object will also display the `venue_name` and `venue_address`, but is using the name and address of the geocoder's found venue. Check the `venue_name` and `venue_address` in the response object to verify if the correct venue has been forecasted.
 &nbsp;
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>
 Private API Key. See more info on [API keys](#api-reference)
 &nbsp;
- **collection_id** `string` <span style="color:blue">OPTIONAL</span>
 Add a venue to an existing collection. See more info on [Collections](#venue-collections)
 &nbsp;
- **venue_id** `string` <span style="color:blue">OPTIONAL</span>
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues. To use the `venue_id` as input, the venue needs to be forecasted before. When the `venue_id` parameter is omitted the `venue_name` and `venue_address` parameters are required.
 &nbsp;

<aside class="notice">
New forecast endpoint: https://besttime.app/api/v1/forecasts
</aside>

<aside class="notice">
HTTP method: POST
</aside>

<aside class="warning">
By default the API is limited to 10 requests per second. Contact us for higher limits.
</aside>


### Response attributes New Forecast <a name="#response-attributes-new-forecast"></a>

- **analysis** `list`
 List with an analysis object for each day of the week, containing analysis like 'peak_hours', 'busy_hours', etc per day. The list contains days `object` and are sorted on day of the week: `day_int` `0` (Monday) to `6` (Sunday).
 &nbsp;
 - analysis[day_int].**busy_hours** `list`
   List with busy hours of the day. The hours are in 24 hour `int` notation.
  &nbsp;
 - analysis[day_int].**day_info** `object`
   Details about the day.
  &nbsp;
     - analysis[day_int].day_info.**day_int** `int`
       Day integer range `0` (Monday) to `6` (Sunday)
       &nbsp;
     - analysis[day_int].day_info.**day_rank_max** `int`
       Day ranking based on maximum busyness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most busy day of the week.
       &nbsp;
     - analysis[day_int].day_info.**day_rank_mean** `int`
       Day ranking based on mean busyness (total volume) of the day. Range `1` to `7`. E.g. `7` indicates the least busy day of the week.
       &nbsp;
     - analysis[day_int].day_info.**day_text** `string`
       Day name. E.g. `monday`
       &nbsp;
     - analysis[day_int].day_info.**venue_closed** `int`/`string` <span style="color:red">DEPRECATED</span>
       Hour of day when the venue closes. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day. Deprecated, use `venue_open_close_v2` instead.
       &nbsp;
     - analysis[day_int].day_info.**venue_open** `int`/`string` <span style="color:red">DEPRECATED</span>
       Hour of day when the venue opens. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day. Deprecated, use `venue_open_close_v2` instead.
       &nbsp;
     - analysis[day_int].day_info.**venue_open_close_v2** `object`
       Object with open and close times for the venue. The object contains two lists: `24h` and `12h`. The `24h` list contains open and close times for the venue in 24 hour notation. The `12h` list contains open and close times for the venue in 12 hour notation. A venue can have multiple opening times per day. Note: requires refreshing the foot traffic forecast if the foot traffic forecast is outdated.
        &nbsp;
        - analysis[day_int].day_info.venue_open_close_v2.**24h** `list`
          List with open and close times objects for the venue in 24 hour notation.
          &nbsp;
        - analysis[day_int].day_info.venue_open_close_v2.**12h** `list`
          List with open and close times for the venue in 12 hour notation.
          &nbsp;
 - analysis[day_int].**day_raw** `list`
   List of raw busyness data for each hour of the day, or within the selected hour range. The list contains percentages ranging from `0` to `100`. Indicating the busyness percentage. Percentages are based on historical visits for the given hour, relative to the biggest peak of the week for this venue. When the `now` or `live` parameter is `true` the list will contain one `int` for the current hour in the local time.
    &nbsp;
 - analysis[day_int].**hour_analysis** `list`
   List with hour objects, containing details per hour.
  &nbsp;
     - analysis[day_int].hour_analysis.**hour** `int`
       Hour integer range `0` (midnight) to `23` (11pm). Please note that the day window within a weekday starts at 6AM `hour = 6` and ends at 5AM `hour = 5` next day. See Introduction section [Forecast day window and weekdays](#forecast-day-window-and-weekdays)
       &nbsp;
     - analysis[day_int].hour_analysis.**intensity_nr** `int`
       Hour intensity_nr indicates how busy the venue is on a scale of 5, ranging from `-2` to `2`. When the venue is closed at the given hour it indicates `999`. See `intensity_txt` for the textual version of the same scale.
       &nbsp;
     - analysis[day_int].hour_analysis.**intensity_txt** `string`
       Hour intensity_txt indicates how busy the venue is on a scale of 5. See `intensity_nr` for the integer version of the same scale. The intensity is either `Low`, `Below average`, `Average`, `Above average`, or `High`. When the venue is closed at the given hour it indicates `Closed`.
       &nbsp;
 - analysis[day_int].**peak_hours** `list`
   List with peak objects, containing details of one or multiple peaks per day.
  &nbsp;
     - analysis[day_int].peak_hours.**peak_start** `int`
       Start hour of the peak, using the 24 hour notation.
       &nbsp;
     - analysis[day_int].peak_hours.**peak_max** `int`
       Hour of the day when the peak is at its maximum. Using the 24 hour notation.
       &nbsp;
     - analysis[day_int].peak_hours.**peak_end** `int`
       End hour of the peak, using the 24 hour notation.
       &nbsp;
     - analysis[day_int].peak_hours.**peak_intensity** `int`
       Intensity of the peak, rated from `1` (minimum) to `5` (maximum)
       &nbsp;
     - analysis[day_int].peak_hours.**peak_delta_mean_week** `int`
       Percentage how much the peak maximum is above the mean busyness of the week.
       &nbsp;
 - analysis[day_int].**quiet_hours** `list`
   List with quiet hours of the day. The hours are in 24 hour `int` notation.
  &nbsp;
 - analysis[day_int].**surge_hours** `object`
   Details at which hour most people enter (come) or leave the venue.
  &nbsp;
     - analysis[day_int].surge_hours.**most_people_come** `int`
       Hour when most people come to the venue during the day window. The hours are in 24 hour `int` notation.
       &nbsp;
     - analysis[day_int].surge_hours.**most_people_leave** `int`
       Hour when most people leave to the venue during the day window. The hours are in 24 hour `int` notation.
       &nbsp;
- **epoch_analysis** `int`
 Epoch timestamp when the forecast was made.
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
 - venue_info.**venue_address** `string`
   Address of the venue. This is the address of the venue as found by the geocoding lookup. Note this address could be different than the `venue_address` used as input.
  &nbsp;
 - venue_info.**venue_id** `string`
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is the primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.
  &nbsp;
 - venue_info.**venue_dwell_time_min** `int`
   Minimum usual visitor dwell time in minutes, or `0` when not available.
  &nbsp;
 - venue_info.**venue_dwell_time_max** `int`
   Maximum usual visitor dwell time in minutes, or `0` when not available.
  &nbsp;
 - venue_info.**venue_dwell_time_avg** `int`
   Average usual visitor dwell time in minutes, or `0` when not available.
  &nbsp;
  - venue_info.**venue_dwell_time_avg** `int`
   Average usual visitor dwell time in minutes, or `0` when not available.
  &nbsp;
  - venue_info.**venue_type** `string`
   Type of venue, or `OTHER` when not available. Possible types are (most common shown first) `RESTAURANT, SHOPPING, FAST_FOOD, BAR, SUPERMARKET, GROCERY, PARK, OTHER, APPAREL, FOOD_AND_DRINK, CAFE, SHOPPING_CENTER, COFFEE, AIRPORT, SPORTS_COMPLEX, PHARMACY, PERSONAL_CARE, VEHICLE, GAS_STATION, MUSEUM, DENTIST, LIBRARY, BANKING, TOURIST_DESTINATION, CASH_MACHINE, FOOD_DELIVERY, EVENT_VENUE, SPA, MARKET, CLUBS, PUBLIC_TRANSIT, BREWERY, SPORTING_GOODS, HISTORICAL, PERFORMING_ARTS, DOCTOR, AMUSEMENT_PARK, GIFTS, TEA, CHURCH, SKILL_INSTRUCTION, TRAIN_STATION, ARTS, GOLF, ZOO, BOTANICAL_GARDEN, NATIONAL_PARK, SUBWAY_STATION, CASINO, MOVIE_THEATER, POST_OFFICE, HIKING, GOLF_COURSE, NATURE_RESERVE, BRIDGE, BUS_STATION, GOVERNMENT, REST_AREA, WINERY, SCENIC_POINT, SOUVENIR_SHOP, CITY_HALL, BOATING, CONCERT_HALL, SWIMMING, MONUMENT, SOCCER, CAR_RENTAL, MOSQUE, INDUSTRIAL, VISITOR_CENTER, ANTIQUES, AQUARIUM, PALACE, HINDU_TEMPLE, STADIUM, WINTER_SPORTS, BUDDHIST_TEMPLE, EMBASSY, TEMPLE, TENNIS, BASEBALL, FERRY_TERMINAL, FISHING, POLICE, SCHOOL, BAKERY, AGRICULTURE, CRICKET, FAIRGROUNDS, GONDOLA_LIFT_STATION, HOSPITAL, LIGHTHOUSE, MILITARY, MORMON_TEMPLE, UNIVERSITY`
  &nbsp;
- venue_info.**venue_types** `list`
   Detailed venue types/services (not to confuse with `venue_type`)
  &nbsp;
- venue_info.**venue_lat** `float`
   Geographic latitude of the venue.
  &nbsp;
- venue_info.**venue_lng** `float`
   Geographic longitude of the venue.
  &nbsp;
- venue_info.**rating** `float`
   Average rating of the venue. Possible values are `2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0`, or `0` when not available.
  &nbsp;
- venue_info.**reviews** `int`
   Total number of reviews for the venue, or `0` when not available.
  &nbsp;
- venue_info.**price_level** `int`
   Price level of the venue ranging from `1` (least expensive) to `5` (most expensive), or `0` when not available.
  &nbsp;


<!-- Content from _forecastliveendpoints.md -->


# Live foot-traffic data

> Returns Live foot-traffic data for a venue based on the venue name and address:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/live"

params = {
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
    'venue_name': 'McDonalds',
    'venue_address': 'Ocean Ave, San Francisco'
}

response = requests.request("POST", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request POST 'https://besttime.app/api/v1/forecasts/live?
api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&
venue_name=McDonalds&
venue_address=Ocean%20Ave%2C%20San%20Francisco'
```

```javascript
const params = new URLSearchParams({ 
  'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
  'venue_name': 'McDonalds',
  'venue_address': 'Ocean Ave, San Francisco'
});

fetch(`https://besttime.app/api/v1/forecasts/live?${params}`, {
  method: 'POST'
}).then(function(data) { 
  console.log(data); 
});
```

The 'live forecast' endpoint is used to get live information of the venue. Life forecasts are either created using the venue name and address, or the venue_id as input in the request. The response includes information regarding the live busyness at this moment compared to the forecasted busyness of the corresponding hour.  

When creating a live forecast the normal forecast for the venue will NOT be updated. Use one of the other New Forecast endpoints

<b>Highly recommended to read first:
- [BestTime tools beginners tutorial](https://blog.besttime.app/foot-traffic-nightlife-bars/)
- [BestTime Software API beginners tutorial](https://blog.besttime.app/beginners-guide-foot-traffic-data-software-api/)
- [HTML/ Javascript examples](#examples)
</b>  



### Input attributes Live foot traffic data

- **venue_id** `string` <span style="color:blue">RECOMMENDED/OPTIONAL</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues. To use the `venue_id` as input, the venue needs to be forecasted before. When the `venue_id` parameter is omitted the `venue_name` and `venue_address` parameters are required. We recommend using the venue_id for faster responses and when using a package subscription to stay within the subscription limits. 
 &nbsp;
- **venue_name** `string` <span style="color:blue">OPTIONAL</span>  
 Name of the venue (public business). Max input length `256` characters.  When then using the `venue_id` the `venue_name` and `venue_address` can be omitted. Highly recommend to use the `venue_id` (instead of name and address) for faster responses and when using a package subscription to stay within the subscription limits.
 &nbsp; 
- **venue_address** `string` <span style="color:blue">OPTIONAL</span>  
 Address of the venue (public business). The address does not have to be exact, but needs to be precise enough for the geocoder engine to find the correct venue. The more specific the address the higher chance the geocoder will find the venue. Max input length `1024` characters. The response object will also display the `venue_name` and `venue_address`, but is using the name and address of the geocoder's found venue. Check the `venue_name` and `venue_address` in the response object to verify if the correct venue has been forecasted.  
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
        "venue_dwell_time_avg": 40,
        "rating": 3.5,
        "reviews": 1204,
        "price_level": 1
    }
}
```

### Response attributes Live Forecast <a name="#response-attributes-live-forecast"></a>

- **analysis** `object`  
 Object with live analysis details.  
 &nbsp; 
 - analysis.**venue_forecasted_busyness** `int`  
   Forecasted busyness for this hour, based on the weekly forecast. Ranging from `0` to `100`.  
  &nbsp;
 - analysis.**venue_live_busyness** `int`  
   Live busyness at the venue for current, based on the weekly forecast.  
   In most cases, the live percentage will be between 0% and 100%. However, a value above 100%
   means it is busier than the highest forecasted peak of the week. E.g. 200% meaning it is two times as busy as the normal forecasted peak (100%) of the week. 
  &nbsp;
 - analysis.**venue_live_busyness_available** `bool`  
   Indicates if there is live data available for this venue at this moment.  
  &nbsp;
 - analysis.**venue_forecast_busyness_available** `bool`  
   Indicates if there is forecast data available for this venue at this moment. The forecast value can be used as the alternative when there is no live data available.
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
   Minimum usual visitor dwell time in minutes, or `0` when not available.  
  &nbsp;
 - venue_info.**venue_dwell_time_max** `int`  
   Maximum usual visitor dwell time in minutes, or `0` when not available.   
  &nbsp;
 - venue_info.**venue_dwell_time_avg** `int`  
   Average usual visitor dwell time in minutes, or `0` when not available.   
  &nbsp;
 - venue_info.**rating** `float`
    Average rating of the venue. Possible values are `2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0`, or `0` when not available.
   &nbsp;
  - venue_info.**reviews** `int`
    Total number of reviews for the venue, or `0` when not available.
   &nbsp;
  - venue_info.**price_level** `int`
    Price level of the venue ranging from `1` (least expensive) to `5` (most expensive), or `0` when not available.
   &nbsp;

<!-- Content from _gettingstarted.md -->

# Getting started

## API keys

## New forecast

## Query venue

<!-- Content from _introduction.md -->


# Introduction

Welcome to the BestTime.app documentation! The documentation includes different sections.

* What is BestTime.app (see below)
* [API reference](#api-reference)


## What is BestTime.app?
BestTime.app is a foot traffic data (API) service that forecasts how busy a public business (venues) will be at any given hour of the week. 
The data is provided for 150+ countries using anonymous phone signals, and is available for retail, restaurants, bars, gyms, museums, and more. 
Foot traffic forecasts are based on average visits over the past weeks. 
Busyness for any given hour is predicted relative to the biggest peak of the week for this business. 
The foot traffic data is presented as percentages for each hour of the week from 0% (empty/ closed) to 100% (visitor peak of the week). 

<b>Highly recommended to read:
- [BestTime tools beginners tutorial](https://blog.besttime.app/foot-traffic-nightlife-bars/)
- [BestTime Software API beginners tutorial](https://blog.besttime.app/beginners-guide-foot-traffic-data-software-api/)
</b>

Additional BestTime functionality:
<ul>
<li>Live updates - know if a venue is more or less busy than normal (not available for all venues).</li>
<li>Foot traffic analyses, like peak hours, quiet hours, week overviews</li>
<li>Search foot traffic based on category (e.g. supermarkets in London) or name (e.g. McDonalds in San Francisco).
</li>
<li>
    Filter and sort venues in a whole area based on foot traffic data, dwell time, day, time, and business type, location, and more.
</li>
<li>Integrate all data directly into your applications/ research using the developer REST-API.
</li>
</ul>
You could compare it with a supercharged FourSquare foot traffic data/ Google Popular Times API with more footfall data analytic functionality.


## Use cases
Below are a few example use-cases how the analyzed data can be used in real-world:

- Inform visitors what the best time is to visit a venue.
- Find the most popular hours of a bar nearby. This way you will never end up in an empty bar, and never end up in the queue.
- Find the quietest gym by comparing multiple gyms in your neighborhood.
- Find the best time to go to a museum and avoid the queue.
- Find out of a venue is more crowded than normal at this moment with the live data.
- Create a dashboard for your venue (e.g. reception, kitchen, etc) to keep your employees informed how busy it is now (live), how busy it will be next hour (forecasted), and when the next peak is coming.
- Compare your business with the competitors to find the perfect time to launch a promotion.
- Behavioral research: Get insights on how people behave in certain areas. E.g. in general gyms tend to peak around 7 am and 7 pm, restaurants tend to peak around 1 pm and 9 pm, shops tend to peak around 4 pm.


## Forecasts

A forecast can be made by giving the name and the approximate address of the public business. BestTime.app will try to find the correct business. If there is enough data available it will analyse the data and create a forecast. 

### Public businesses
BestTime.app works in general only for public businesses. For example:

* Restaurants
* Bars
* Gyms
* Shops
* Museums
* Theatres
* Malls
* Beaches
* Supermarkets
* Public offices (like customer service points)
* Theme parks

### Results
A forecast is usually created within a few seconds and responds with all primary analyses. Additionally, a forecast is stored on the server so it can be queried later again without the need to forecast the business again.

The forecast results include:

- Relative foot traffic intensity percentage data for every hour of the week ranging from 0 to 100% (wherein 100% is the forecasted peak hour of the week)
- Week analysis
    - Peak busyness per day percentage
    - Average busyness (volume) per day percentage
    - Ranking based on the maximum peak of the day
    - Ranking based on the total visitor's volume of the day
- Hour analysis
    - How busy each hour of the day will be (rated from -2 to +2)
- Peak analysis
    - Start time of the peak
    - Time of the peak (maximum)
    - End time of the peak
    - Peak intensity (rated from 1 to 5)
- Surge analysis
    - What time are most people going to the business 
    - What time are most people leaving the business
- Busy hours
    - List of all busy hours per day.
- Quiet hours
    - List of all quiet hours per day.

### Relative numbers

BestTime.app does not provide absolute business visitor numbers. Data in the forecasts represent an approximate how busy a business will be in a relative number. Each hour of the week is rated on a five-point scale from -2 to +2 (Low, below average, average, above average, high). The rating is also depending on the mean busyness of the week.

### Coverage
BestTime.app has coverage in 150+ countries. It depends on multiple factors if a business can be forecasted. A rough guideline is that the business needs to be a public business and has at least 100 visitors per day. 


### Updating venue foot traffic data
- Live data needs to be refreshed every clock hour using the Live data endpoint.
- A foot traffic forecast can be used for one or multiple weeks. To update an existing business forecast you need to create a 'New venue foot traffic data forecast'.
* The venue filter returns updated foot traffic data that is never older than a month. If you want the latest foot traffic data you can use the 'New venue foot traffic data forecast' to update a single venue, or the Venue Update tool to update multiple venues.

## Queries
Forecasting a (new) business takes a few seconds (using the New Foot Traffic forecast endpoint). Normally a forecast is accurate for at least several weeks (depending on the business), therefore the data from existing forecasts can still be used for a longer period. Queries are used to get data from an existing forecasted business. For example the whole forecast, or a specific analysis on a specific day.

A query response is almost instant, includes sometimes additional data, and makes it easier to answer specific questions.

### Recommended usage
Forecasts are based on visits to the business from the past few weeks. We recommend therefore to only forecast (update) a business once every few weeks. Queries should be used in between the forecasts. This reduces API forecast credits and improves the API performance. The Venue filter tool is the most cost/speed effective method to get foot traffic data for multiple venues. Live data needs to be updated every clock hour and is therefore relatively expensive compared to using the Venue filter API and / or the New Foot Traffic forecast endpoint - which returns data that is useful for a week or longer.

### Additional dynamic data
Some query responses include additional dynamic data on top of the stored forecast. 
The peak-, surge-, busy-, quiet analysis query responses include the time remaining until the next event (e.g. 2,5 hours until the first busy hour).

### Query analysis
BestTime.app has several query endpoints:

Venue queries:
- Query the details of a specific venue
- Query all forecasted venues
- Query all venues matching the busyness, location, time & day, and/or type filter

Forecast of a single venue queries:
- Query the whole original forecast (includes all analysis) of a venue
- Query a specific day of the week (includes all analysis)
- Query a specific hour of the day 
- Query the current hour of the business with the local business timezone taken into account (or X hours ahead from the current hour)
- Query the busy hours of today (or X days ahead from today)
- Query the quiet hours of today (or X days ahead from today)
- Query the peak hours of today (or X days ahead from today)
- Query the surge hours of today (or X days ahead from today)


## Forecast day window and weekdays
BestTime.app uses a 24-hour notation, displayed from `0` to `23`. Where `0` indicates midnight and `23` indicates 11 PM. 
Important to know is that the foot traffic data time window ranges from 6 AM until 5 AM next day. Not from midnight to midnight. This is for example useful for public venues with late opening times like bars and nightclubs. 

Below is an example how an array of 24 foot traffic percentages relate to the hour of the day , and the index of the array (from 0 - 23). The foot traffic data is just an example for a restaurant that opens at 9PM (array index 3) has a lunch peak 1 PM (array index 7),  a dinner peak at 9 PM (array index 15) and closes at 3 AM (array index 21).  


| Hour | Index | Foot Traffic (Example) |
|------|-------|------------------------|
| 6 AM  | 0     | 0                      |
| 7 AM  | 1     | 0                      |
| 8 AM  | 2     | 0                      |
| 9 AM  | 3     | 10                     |
| 10 AM | 4     | 15                     |
| 11 AM | 5     | 35                     |
| 12 PM | 6     | 50                     |
| 1 PM  | 7     | 65                     |
| 2 PM  | 8     | 45                     |
| 3 PM  | 9     | 35                     |
| 4 PM  | 10    | 30                     |
| 5 PM  | 11    | 35                     |
| 6 PM  | 12    | 45                     |
| 7 PM  | 13    | 60                     |
| 8 PM  | 14    | 85                     |
| 9 PM  | 15    | 90                     |
| 10 PM | 16    | 80                     |
| 11 PM | 17    | 55                     |
| 12 AM | 18    | 40                     |
| 1 AM  | 19    | 30                     |
| 2 AM  | 20    | 20                     |
| 3 AM  | 21    | 0                      |
| 4 AM  | 22    | 0                      |
| 5 AM  | 23    | 0                      |


<!-- Content from _queryendpoints.md -->

# Query endpoints

All query endpoints are used to retrieve all data or specific analysis from an existing forecast. Query endpoints often also include dynamic information (e.g. remaining time until it will be busy according to the forecast).
The `venue_id` is the primary parameter to query an existing forecast. 

It is also possible to update a venue forecast in combination with the query in one API call. This way you can retrieve query-specific data:
-  with a fresh forecast

Check the query endpoint itself for more information. This will be counted as new forecast credit.


Query endpoints:  

**Venues**
Lists all previously forecasted venues, and venue_id's.

**Venues filtered (Radar tool)**
Query earlier forecasted venues that match the filter on busyness, location, time, day and venue type.

**Venue**
Query a forecasted venue, with detailed venue information.  

**Week**
Query the forecast for the whole week, including all analysis. This gives the same response as the original 'new forecast' endpoint.  

**Week raw**
Query the forecast for the whole week, in raw percentages. 

**Week overview**
Qeury a week overview for the venue. Including day maximum, day mean, day maximum ranking, day mean ranking, and open/closing times.

**Day**
Query a specific day of the week including all analysis.  

**Day raw**
Query the forecast for a specific day of the week, in raw percentages. 

**Hour**
Query a specific hour of the day.  

**Hour raw**
Query the forecast for a specific day and hour of the week, in raw percentages.  

**Now**
Query the current hour of the business with the local business timezone taken into account. 

**Now raw**
Query the current hour of the business with the local business timezone taken into account, in raw percentages. 

**Peak Hours**
Query the peak hours of today. Peaks will also include peak start, end times, and how intense the peak will be.

**Busy Hours**
Query the busy hours of today.  

**Quiet Hours**
Query the quiet hours of today.  

**Surge Hours**
Query the surge hours of today. Surge analysis shows when most people come to a venue, or leave the venue.  

<b>Highly recommended to read first:
- [BestTime tools beginners tutorial](https://blog.besttime.app/foot-traffic-nightlife-bars/)
- [BestTime Software API beginners tutorial](https://blog.besttime.app/beginners-guide-foot-traffic-data-software-api/)
</b>

<!-- Content from _queryendpointsbusyhours.md -->

# Query busy hours

> Query busy hours:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/busy"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_step': 0
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/busy?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&
day_step=0'
```

```javascript
const params = new URLSearchParams({ 
  'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
  'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
  'day_step': 0
});

fetch(`https://besttime.app/api/v1/forecasts/busy?${params}`, {
  method: 'get'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes Query Busy hours

The 'query busy hours' endpoint is used to retrieve all busy hour information from an existing forecast for a specific day of the week.
By default, the response includes the busy hour information for the current day (at the local timezone of the venue). 

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
 - **day_int** `int` <span style="color:blue">OPTIONAL</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday). `day_int` cannot be used in combination with `day_step` and `hour_step`.  
 &nbsp; 
- **day_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the day (day of week of the venue in the local timezone). E.g. `0` means current day, and `1` means tomorrow. Range: min `-31`, max `31`. `day_step` cannot be used in combination with `day_int`.  
 &nbsp;  
- **hour_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the hour (hour of the venue in the local timezone). E.g. `0` means current hour, and `-2` means two hours ago. Range: min `-12`, max `12`. `hour_step` cannot be used in combination with `day_int`.  
 &nbsp;
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Query busy hours endpoint: https://besttime.app/api/v1/forecasts/busy
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON response like this:

```json
{
    "analysis": {
        "busy_hours": [
            {
                "busy_end": 14,
                "busy_end_12": "2PM",
                "busy_end_in": "2 hour and 16 minutes",
                "busy_end_in_sec": 8220,
                "busy_end_passed": 0,
                "busy_period_duration": 4,
                "busy_start": 10,
                "busy_start_12": "10AM",
                "busy_start_in": "Start of busy period already passed",
                "busy_start_in_sec": 0,
                "busy_start_passed": 1
            },
            {
                "busy_end": 20,
                "busy_end_12": "8PM",
                "busy_end_in": "8 hour and 16 minutes",
                "busy_end_in_sec": 29820,
                "busy_end_passed": 0,
                "busy_period_duration": 4,
                "busy_start": 16,
                "busy_start_12": "4PM",
                "busy_start_in": "4 hour and 16 minutes",
                "busy_start_in_sec": 15420,
                "busy_start_passed": 0
            }
        ],
        "busy_hours_list": [
            10,
            11,
            12,
            13,
            16,
            17,
            18,
            19
        ],
        "busy_hours_list_12h": [
            "10AM",
            "11AM",
            "12PM",
            "1PM",
            "4PM",
            "5PM",
            "6PM",
            "7PM"
        ],
        "busy_hours_list_coming": [
            12,
            13,
            16,
            17,
            18,
            19
        ],
        "busy_hours_list_coming_12h": [
            "12PM",
            "1PM",
            "4PM",
            "5PM",
            "6PM",
            "7PM"
        ],
        "day_info": {
            "day_int": 4,
            "day_rank_max": 7,
            "day_rank_mean": 3,
            "day_text": "Friday",
            "venue_closed": 4,
            "venue_open": 4
        }
    },
    "epoch_analysis": 1583911633,
    "forecast_updated_on": "2020-03-11T07:27:13.849228+00:00",
    "status": "OK",
    "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
    "venue_info": {
        "venue_current_gmttime": "Fri, 13 Mar 2020 18:43:30 GMT",
        "venue_current_localtime_iso": "2020-03-13T11:43:30.101057-07:00",
        "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles"
    },
    "venue_name": "McDonald's"
}
```

### Response attributes Query Busy hours

- **analysis** `object`  
 Containing the all the busy hour analysis and venue day info.
 - analysis.**busy_hours** `list`  
   List with busy hour objects, containing details of one or multiple busy periods per day.  
  &nbsp;
     - analysis.busy_hours.**busy_start** `int`  
       Start hour of the busy hour, using the 24 hour notation.  
       &nbsp;
     - analysis.busy_hours.**busy_start_passed** `int`  
       Indicates if the busy hour start is already passed. Indicates `1` for passed, `0` for not passed.
       &nbsp;
     - analysis.busy_hours.**busy_start_12** `string`  
       Start hour of the busy hour, using the 12 hour notation.  
       &nbsp;
     - analysis.busy_hours.**busy_start_in** `string`  
       Time remaining until the busy hour starts. Notation 'HH hour and MM minutes'. If busy hour start has been passed it will indicate `Start of busy period already passed`  
       &nbsp;
     - analysis.busy_hours.**busy_start_in_sec** `int`  
       Time remaining until the busy hour starts, in seconds.  
       &nbsp;
     - analysis.busy_hours.**busy_period_duration** `int`  
       Duration of the busy period, in hours.  
       &nbsp;
     - analysis.busy_hours.**busy_end** `int`  
       End hour of the busy hour, using the 24 hour notation.  
       &nbsp;
     - analysis.busy_hours.**busy_end_passed** `int`  
       Indicates if the busy hour end is already passed. Indicates `1` for passed, `0` for not passed.
       &nbsp;
     - analysis.busy_hours.**busy_end_12** `string`  
       End hour of the busy hour, using the 12 hour notation.  
       &nbsp;
     - analysis.busy_hours.**busy_end_in** `string`  
       Time remaining until the busy hour ends. Notation 'HH hour and MM minutes'. If busy hour end has been passed it will indicate `End of busy period already passed`  
       &nbsp;
     - analysis.busy_hours.**busy_end_in_sec** `int`  
       Time remaining until the busy hour ends, in seconds.  
       &nbsp;
 - analysis.**busy_hours_list** `list`  
   List with busy hours (`int`), in 24-hour notation.  
  &nbsp;
 - analysis.**busy_hours_list_12h** `list`  
   List with busy hours (`string`), in 12-hour notation.  
  &nbsp;
 - analysis.**busy_hours_list_coming** `list`  
   List with busy hours (`int`) which still have to come. In 24-hour notation.  
  &nbsp;
 - analysis.**busy_hours_list_coming_12h** `list`  
   List with busy hours (`string`) which still have to come, in 12-hour notation.  
  &nbsp;
- analysis.**day_info** `object`  
   Details about the day    
  &nbsp;
     - analysis.day_info.**day_int** `int`  
       Day integer range `0` (Monday) to `6` (Sunday)  
       &nbsp;
     - analysis.day_info.**day_rank_max** `int`  
       Day ranking based on the maximum busyness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most busy day of the week.  
       &nbsp;
     - analysis.day_info.**day_rank_mean** `int`  
       Day ranking based on mean busyness (total volume) of the day. Range `1` to `7`. E.g. `7` indicates the least busy day of the week.  
       &nbsp;
     - analysis.day_info.**day_text** `string`  
       Day name. E.g. `monday`  
       &nbsp;
     - analysis.day_info.**venue_closed** `int`/`string`  
       Hour of day when the venue closes. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.  
       &nbsp;
     - analysis.day_info.**venue_open** `int`/`string`  
       Hour of day when the venue opens. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.  
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
- **venue_info** `object`  
 Details of the forecasted venue.  
 &nbsp; 
  - venue_info.**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup. Note this name could be slightly different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_address** `string`  
   Address of the venue. This is the address of the venue as found by the geocoding lookup. Note this address could be different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_current_gmtttime** `string`  
   Time at the venue in Greenwich Mean Time. Adjusting the `hour_step` and `day_step` will also alter this time.  
 - venue_info.**venue_current_localtime_iso** `string`  
   Local time at the venue. Adjusting the `hour_step` and `day_step` will also alter this time.  
  &nbsp;
 - venue_info.**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is the primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.
  &nbsp;
 - venue_info.**venue_timezone** `string`  
   The timezone of the venue. E.g. `America/Los Angeles`  
  &nbsp;

### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/busy`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.



<!-- Content from _queryendpointsday.md -->

# Query day 

> Query one day of the week:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/day"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_int': 3
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/day?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&
day_int=3'
```

```javascript
const params = new URLSearchParams({ 
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_int': 3
});

fetch(`https://besttime.app/api/v1/forecasts/day?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes Query Day

The 'query day' endpoint is used to retrieve all analysis from an existing forecast for a specific day of the week.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **day_int** `int` <span style="color:blue">OPTIONAL</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday). If not specified, the current day (in local time of the venue) of the week is used.  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Query day endpoint: https://besttime.app/api/v1/forecasts/day
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON response like this:

```json
  {
  "analysis": {
    "busy_hours": [
      9,
      10,
      11
    ],
    "day_info": {
      "day_int": 0,
      "day_rank_max": 6,
      "day_rank_mean": 4,
      "day_text": "Monday",
      "venue_closed": 4,
      "venue_open": 4
    },
    "hour_analysis": [{
        "hour": 6,
        "intensity_nr": -1,
        "intensity_txt": "Below average"
      },
      {
        "hour": 7,
        "intensity_nr": -1,
        "intensity_txt": "Below average"
      },
      {
        "hour": 8,
        "intensity_nr": 0,
        "intensity_txt": "Average"
      },
      ....Other hours hidden. See below for the full JSON response example...
      {
        "hour": 5,
        "intensity_nr": -1,
        "intensity_txt": "Below average"
      }
    ],
    "peak_hours": [{
      "peak_delta_mean_week": 29,
      "peak_end": 23,
      "peak_intensity": 4,
      "peak_max": 11,
      "peak_start": 8
    }],
    "quiet_hours": [
      2,
      3,
      4,
      5
    ],
    "surge_hours": {
      "most_people_come": 8,
      "most_people_leave": 0
    }
  },
  "day_int": 0,
  "epoch_analysis": 1583400856,
  "forecast_updated_on": "2020-03-05T09:34:16.836061+00:00",
  "status": "OK",
  "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
  "venue_name": "McDonald's"
}
```

> Click <a href="https://github.com/besttime-app/slate/blob/master/source/examples/query_day/query_day_response.json" target="_blank">here</a> for the full JSON response


### Response attributes Query Day

- **analysis** `object`  
 Containing the all the included analytics like 'peak_hours', 'busy_hours', etc for the given day. 
 - analysis.**busy_hours** `list`  
   List with busy hours of the day. The hours are in 24 hour `int` notation.  
  &nbsp;
 - analysis.**day_info** `object`  
   Details about the day    
  &nbsp;
     - analysis.day_info.**day_int** `int`  
       Day integer range `0` (Monday) to `6` (Sunday)  
       &nbsp;
     - analysis.day_info.**day_rank_max** `int`  
       Day ranking based on the maximum busyness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most busy day of the week.  
       &nbsp;
     - analysis.day_info.**day_rank_mean** `int`  
       Day ranking based on mean busyness (total volume) of the day. Range `1` to `7`. E.g. `7` indicates the least busy day of the week.  
       &nbsp;
     - analysis.day_info.**day_text** `string`  
       Day name. E.g. `monday`  
       &nbsp;
     - analysis.day_info.**venue_closed** `int`/`string`  
       Hour of day when the venue closes. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.  
       &nbsp;
     - analysis.day_info.**venue_open** `int`/`string`  
       Hour of day when the venue opens. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.  
       &nbsp;
 - analysis.**hour_analysis** `list`  
   List with hour objects, containing details per hour.  
  &nbsp;
     - analysis.hour_analysis.**hour** `int`  
       Hour integer range `0` (midnight) to `23` (11pm). Please note that the hour window within a weekday starts at 6AM `hour = 6` and ends at 5AM `hour = 5`. See Introduction section [Forecast day window and weekdays](#forecast-day-window-and-weekdays)  
       &nbsp;
     - analysis.hour_analysis.**intensity_nr** `int`  
       Hour intensity_nr indicates how busy the venue is on a scale of 5, ranging from `-2` to `2`. When the venue is closed at the given hour it indicates `999`. See `intensity_txt` for the textual version of the same scale.  
       &nbsp;
     - analysis.hour_analysis.**intensity_txt** `string`  
       Hour intensity_txt indicates how busy the venue is on a scale of 5. See `intensity_nr` for the integer version of the same scale. The intensity is either `Low`, `Below average`, `Average`, `Above average`, or `High`. When the venue is closed at the given hour it indicates `Closed`.  
       &nbsp;
 - analysis.**peak_hours** `list`  
   List with peak objects, containing details of one or multiple peaks per day.  
  &nbsp;
     - analysis.peak_hours.**peak_start** `int`  
       Start hour of the peak, using the 24 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_max** `int`  
       Hour of the day when the peak is at its maximum. Using the 24 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_end** `int`  
       End hour of the peak, using the 24 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_intensity** `int`  
       Intensity of the peak, rated from `1` (minimum) to `5` (maximum)  
       &nbsp;
     - analysis.peak_hours.**peak_delta_mean_week** `int`  
       Percentage how much the peak maximum is above the mean busyness of the week.  
       &nbsp;
 - analysis.**quiet_hours** `list`  
   List with quiet hours of the day. The hours are in 24 hour `int` notation.  
  &nbsp;
 - analysis.**surge_hours** `object`  
   Details at which hour most people enter (come) or leave the venue.
  &nbsp;
     - analysis.surge_hours.**most_people_come** `int`  
       Hour when most people come to the venue during the day window. The hours are in 24 hour `int` notation.  
       &nbsp;
     - analysis.surge_hours.**most_people_leave** `int`  
       Hour when most people leave to the venue during the day window. The hours are in 24 hour `int` notation.  
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
- **venue_info** `object`  
 Details of the forecasted venue.  
 &nbsp; 
  - venue_info.**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup. Note this name could be slightly different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_address** `string`  
   Address of the venue. This is the address of the venue as found by the geocoding lookup. Note this address could be different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is the primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.
  &nbsp;
 - venue_info.**venue_timezone** `string`  
   The timezone of the venue. E.g. `America/Los Angeles`  
  &nbsp;


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/day`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.



<!-- Content from _queryendpointsdayraw.md -->

# Query day raw

> Query the raw day data:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/day/raw"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_int': 3
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/day/raw?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&
day_int=3'
```

```javascript
const params = new URLSearchParams({ 
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_int': 3
});

fetch(`https://besttime.app/api/v1/forecasts/day/raw?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes

The 'query day raw' endpoint is used to retrieve the raw data from an existing forecast for one day of the week.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **day_int** `int` <span style="color:blue">OPTIONAL</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday). If not specified, the current day (in local time of the venue) of the week is used.   
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Day raw endpoint: https://besttime.app/api/v1/forecasts/day/raw
</aside>

<aside class="notice">
HTTP method: GET
</aside>

> The above request returns JSON structured like this:

```json
{
    "analysis": {
        "day_raw": [
            0.0,
            40.0,
            60.0,
            70.0,
            80.0,
            90.0,
            90.0,
            90.0,
            90.0,
            80.0,
            70.0,
            70.0,
            70.0,
            70.0,
            70.0,
            70.0,
            60.0,
            50.0,
            40.0,
            30.0,
            20.0,
            10.0,
            0.0,
            0.0
        ]
    },
    "epoch_analysis": 1585875838,
    "forecast_updated_on": "2020-04-03T01:03:58.685394+00:00",
    "status": "OK"
}
```


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/day/raw`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.



<!-- Content from _queryendpointshour.md -->


# Query hour 

> Query a specific hour of the week:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/hour"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_int': 3,
    'hour':23
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/hour?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&
day_int=3&
hour=23'
```

```javascript
const params = new URLSearchParams({ 
  'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
  'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
  'day_int': 3,
  'hour': 23
});

fetch(`https://besttime.app/api/v1/forecasts/hour?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes Query Hour

The 'query hour' endpoint is used to retrieve the 'hour analysis' forecast for the given hour and day of the week.  

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **day_int** `int` <span style="color:orange">REQUIRED</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday).  
 &nbsp; 
- **hour** `int` <span style="color:orange">REQUIRED</span>  
 Hour of the day. Range `0` (Midnight) to `23` (11pm). Please note that the day window within a weekday starts at 6AM `hour = 6` and ends at 5AM `hour = 5` next day. See Introduction section [Forecast day window and weekdays](#forecast-day-window-and-weekdays)  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Hour forecast endpoint: https://besttime.app/api/v1/forecasts/hour
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON reponse like this:

```json
{
    "analysis": {
        "hour_analysis": {
            "hour": 23,
            "intensity_nr": 0,
            "intensity_txt": "Average"
        }
    },
    "day_int": 3,
    "epoch_analysis": 1583400856,
    "forecast_updated_on": "2020-03-05T09:34:16.842662+00:00",
    "status": "OK",
    "venue_info": {
        "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
        "venue_name": "McDonald's"
    }
}
```

> Click <a href="https://github.com/besttime-app/slate/blob/master/source/examples/query_hour/query_hour_response.json" target="_blank">here</a> for the raw JSON response.

### Response attributes Query Hour
- **analysis** `object`  
 Containing the all the included analytics like 'peak_hours', 'busy_hours', etc for the given day. 
 - analysis.**hour_analysis** `list`  
   List with hour objects, containing details per hour.  
   &nbsp;
    - analysis.hour_analysis.**hour** `int`  
      Hour integer range `0` (midnight) to `23` (11pm). Please note that the hour window within a weekday starts at 6AM `hour = 6` and ends at 5AM `hour = 5`. See Introduction section [Forecast day window and weekdays](#forecast-day-window-and-weekdays)  
      &nbsp;
    - analysis.hour_analysis.**intensity_nr** `int`  
      Hour intensity_nr indicates how busy the venue is on a scale of 5, ranging from `-2` to `2`. When the venue is closed at the given hour it indicates `999`. See `intensity_txt` for the textual version of the same scale.  
      &nbsp;
    - analysis.hour_analysis.**intensity_txt** `string`  
      Hour intensity_txt indicates how busy the venue is on a scale of 5. See `intensity_nr` for the integer version of the same scale. The intensity is either `Low`, `Below average`, `Average`, `Above average`, or `High`. When the venue is closed at the given hour it indicates `Closed`.  
      &nbsp;
- **day_int** `int`  
  Day integer range `0` (Monday) to `6` (Sunday)  
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
- **venue_info** `object`  
 Details of the forecasted venue.  
 &nbsp; 
 - venue_info.**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding  result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.  
  &nbsp;
 - venue_info.**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup. Note this name could be slightly different than the `venue_address` used as input.  
  &nbsp;


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/hour`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.



<!-- Content from _queryendpointshourcurrent.md -->


# Query now

> Query the now:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/now"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/now?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843'
```

```javascript
const params = new URLSearchParams({ 
   'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
});

fetch(`https://besttime.app/api/v1/forecasts/now?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```


### Input attributes Query Now

The 'query now' endpoint is used to retrieve the 'hour analysis' forecast for the current hour. The hour is the venues current hour with the local timezone taken into account.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 
- **hour_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the hour (hour of the venue in the local timezone). E.g. `0` means current hour, and `-2` means two hours ago. Range: min `-12`, max `12`.  
 &nbsp; 

<aside class="notice">
Query current hour endpoint: https://besttime.app/api/v1/forecasts/now
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON response like this:

```json
{
    "analysis": {
        "hour_analysis": {
            "hour": 23,
            "intensity_nr": 0,
            "intensity_txt": "Average"
        }
    },
    "day_int": 3,
    "epoch_analysis": 1583400856,
    "forecast_updated_on": "2020-03-05T09:34:16.842662+00:00",
    "status": "OK",
    "venue_info": {
        "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
        "venue_name": "McDonald's",
        "venue_current_gmttime": "Saturday 2020-04-24 04:03AM",
        "venue_current_localtime_iso": "Saturday 2020-04-24 12:02PM"
    }
}
```

> Click <a href="https://github.com/besttime-app/slate/blob/master/source/examples/query_hour/query_hour_response.json" target="_blank">here</a> for the raw JSON response.

### Response attributes Query Current Hour

The response attributes are the same as the attributes in the 'query hour' endpoint.
See [query hour](#query-hour) response attributes.


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/now`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.



<!-- Content from _queryendpointshourraw.md -->

# Query hour raw

> Query the raw hour data:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/hour/raw"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_int': 3,
    'hour': 16
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/hour/raw?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&day_int=3&hour=16'
```

```javascript
const params = new URLSearchParams({ 
  'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
  'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
  'day_int':3,
  'hour':16
});

fetch(`https://besttime.app/api/v1/forecasts/hour/raw?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes

The 'query hour raw' endpoint is used to retrieve the raw data from an existing forecast for one hour of the day.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **day_int** `int` <span style="color:orange">REQUIRED</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday).  
 &nbsp;
- **hour** `int` <span style="color:orange">REQUIRED</span>  
 Hour of the day. Range `0` (Midnight) to `23` (11pm). Please note that the day window within a weekday starts at 6AM `hour = 6` and ends at 5AM `hour = 5` next day. See Introduction section [Forecast day window and weekdays](#forecast-day-window-and-weekdays)  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Hour raw endpoint: https://besttime.app/api/v1/forecasts/hour/raw
</aside>

<aside class="notice">
HTTP method: GET
</aside>

> The above request returns JSON structured like this:

```json
{
  "analysis": {
    "hour_analysis": {
      "hour": 16,
      "intensity_nr": 0,
      "intensity_txt": "Average"
    },
    "hour_raw": 70
  },
  "epoch_analysis": 1585890444,
  "forecast_updated_on": "2020-04-03T05:07:26.012357+00:00",
  "status": "OK",
  "venue_info": {
    "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
    "venue_name": "McDonald's"
  }
}
```


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/hour/raw`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.



<!-- Content from _queryendpointsnowraw.md -->

# Query now raw

> Query the raw hour data for current hour:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/now/raw"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/now/raw?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843'
```

```javascript
const params = new URLSearchParams({ 
  'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
  'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
});

fetch(`https://besttime.app/api/v1/forecasts/now/raw?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes

The 'query now raw' endpoint is used to retrieve the raw data from an existing forecast for one hour of the day. It automatically determines the current day and hour in the local timezone of the venue.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 
- **hour_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the hour (hour of the venue in the local timezone). E.g. `0` means current hour, and `-2` means two hours ago. Range: min `-12`, max `12`. Useful to for example get the forecast for next hour (+1).  
 &nbsp; 

<aside class="notice">
Now raw endpoint: https://besttime.app/api/v1/forecasts/now/raw
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns JSON structured like this:

```json
{
  "analysis": {
    "hour_analysis": {
      "hour": 16,
      "intensity_nr": 0,
      "intensity_txt": "Average"
    },
    "hour_raw": 70
  },
  "epoch_analysis": 1585890444,
  "forecast_updated_on": "2020-04-03T05:07:26.012357+00:00",
  "status": "OK",
  "venue_info": {
    "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
    "venue_name": "McDonald's",
    "venue_current_gmttime": "Saturday 2020-04-24 04:03AM",
    "venue_current_localtime_iso": "Saturday 2020-04-24 12:02PM"
  }
}
```


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/now/raw`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.



<!-- Content from _queryendpointspeakhours.md -->

# Query peak hours

> Query peaks:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/peaks"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_step': 0,
    'hour_step': 0
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/peaks?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&
day_step=0&
hour_step=0'
```

```javascript
const params = new URLSearchParams({ 
  'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
  'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
  'day_step': 0,
  'hour_step': 0
});

fetch(`https://besttime.app/api/v1/forecasts/peaks?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes Query Peaks

The 'query peaks' endpoint is used to retrieve all peaks from an existing forecast for a specific day of the week.
By default, the response includes the peak objects for the current day (at the local timezone of the venue) `peak_hours`. Additionally, it contains a list with peak objects `peaks_coming` which only contains the peaks from `peak_hours` which have not passed yet.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
 - **day_int** `int` <span style="color:blue">OPTIONAL</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday). `day_int` cannot be used in combination with `day_step` and `hour_step`.  
 &nbsp; 
- **day_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the day (day of week of the venue in the local timezone). E.g. `0` means current day, and `1` means tomorrow. Range: min `-31`, max `31`. `day_step` cannot be used in combination with `day_int`.  
 &nbsp;  
- **hour_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the hour (hour of the venue in the local timezone). E.g. `0` means current hour, and `-2` means two hours ago. Range: min `-12`, max `12`. `hour_step` cannot be used in combination with `day_int`.  
 &nbsp;
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Query peak endpoint: https://besttime.app/api/v1/forecasts/peaks
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON response like this:

```json
{
    "analysis": {
        "day_info": {
            "day_int": 1,
            "day_rank_max": 2,
            "day_rank_mean": 4,
            "day_text": "Tuesday",
            "venue_closed": 4,
            "venue_open": 4
        },
        "peak_hours": [
            {
                "peak_delta_mean_week": 37,
                "peak_end": 18,
                "peak_end_12h": "6PM",
                "peak_end_in": "2 hour and 40 minutes",
                "peak_end_in_sec": 9660,
                "peak_end_passed": 0,
                "peak_intensity": 5,
                "peak_max": 13,
                "peak_max_12h": "1PM",
                "peak_max_in": "Peak maximum already passed",
                "peak_max_in_sec": 0,
                "peak_max_passed": 1,
                "peak_start": 7,
                "peak_start_12h": "7AM",
                "peak_start_in": "Peak already started",
                "peak_start_passed": 1
            },
            {
                "peak_delta_mean_week": 12,
                "peak_end": 23,
                "peak_end_12h": "11PM",
                "peak_end_in": "7 hour and 41 minutes",
                "peak_end_in_sec": 27660,
                "peak_end_passed": 0,
                "peak_intensity": 3,
                "peak_max": 21,
                "peak_max_12h": "9PM",
                "peak_max_in": "5 hour and 41 minutes",
                "peak_max_in_sec": 20460,
                "peak_max_passed": 0,
                "peak_start": 18,
                "peak_start_12h": "6PM",
                "peak_start_in": "2 hour and 40 minutes",
                "peak_start_in_sec": 9660,
                "peak_start_passed": 0
            }
        ]
    },
    "epoch_analysis": 1583400856,
    "forecast_updated_on": "2020-03-05T09:34:16.842016+00:00",
    "status": "OK",
    "venue_info": {
        "venue_current_gmttime": "Tue, 10 Mar 2020 22:19:56 GMT",
        "venue_current_localtime_iso": "2020-03-10T15:19:56.979659-07:00",
        "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles"
    }
}
```

### Response attributes Query Peaks


- **analysis** `object`  
 Containing the all the peak analysis and venue day info.
 - analysis.**day_info** `object`  
   Details about the day    
  &nbsp;
     - analysis.day_info.**day_int** `int`  
       Day integer range `0` (Monday) to `6` (Sunday)  
       &nbsp;
     - analysis.day_info.**day_rank_max** `int`  
       Day ranking based on the maximum busyness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most busy day of the week.  
       &nbsp;
     - analysis.day_info.**day_rank_mean** `int`  
       Day ranking based on mean busyness (total volume) of the day. Range `1` to `7`. E.g. `7` indicates the least busy day of the week.  
       &nbsp;
     - analysis.day_info.**day_text** `string`  
       Day name. E.g. `monday`  
       &nbsp;
     - analysis.day_info.**venue_closed** `int`/`string`  
       Hour of day when the venue closes. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.  
       &nbsp;
     - analysis.day_info.**venue_open** `int`/`string`  
       Hour of day when the venue opens. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.  
       &nbsp;
 - analysis.**peak_hours** `list`  
   List with peak objects, containing details of one or multiple peaks per day.  
  &nbsp;
     - analysis.peak_hours.**peak_start** `int`  
       Start hour of the peak, using the 24 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_start_passed** `int`  
       Indicates if the peak start is already passed. Indicates `1` for passed, `0` for not passed.
       &nbsp;
     - analysis.peak_hours.**peak_start_12** `string`  
       Start hour of the peak, using the 12 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_start_in** `string`  
       Time remaining until the peak starts. Notation 'HH hour and MM minutes'. If peak start has been passed it will indicate `Peak start already passed`  
       &nbsp;
     - analysis.peak_hours.**peak_start_in_sec** `int`  
       Time remaining until the peak starts, in seconds.  
       &nbsp;
     - analysis.peak_hours.**peak_max** `int`  
       Hour of the day when the peak is at its maximum. Using the 24 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_max_passed** `int`  
       Indicates if the peak max is already passed. Indicates `1` for passed, `0` for not passed.  
       &nbsp;
     - analysis.peak_hours.**peak_max_12** `string`  
       Hour of the day when the peak is at its maximum. Using the 12 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_max_in** `string`  
       Time remaining until the peak is at its maximum. Notation 'HH hour and MM minutes'. If peak start has been passed it will indicate `Peak maximum already passed`  
       &nbsp;
     - analysis.peak_hours.**peak_max_in_sec** `int`  
       Time remaining until the peak is at its maximum, in seconds
       &nbsp;
     - analysis.peak_hours.**peak_end** `int`  
       End hour of the peak, using the 24 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_end_passed** `int`  
       Indicates if the peak end is already passed. Indicates `1` for passed, `0` for not passed.  
       &nbsp;
     - analysis.peak_hours.**peak_end_12** `string`  
       End hour of the peak, using the 12 hour notation.  
       &nbsp;
     - analysis.peak_hours.**peak_end_in** `string`  
       Time remaining until the peak ends. Notation 'HH hour and MM minutes'. If peak start has been passed it will indicate `Peak end already passed`  
       &nbsp;
     - analysis.peak_hours.**peak_end_in_sec** `int`  
       Time remaining until the peak ends, in seconds.  
       &nbsp;
     - analysis.peak_hours.**peak_intensity** `int`  
       Intensity of the peak, rated from `1` (minimum) to `5` (maximum)  
       &nbsp;
     - analysis.peak_hours.**peak_delta_mean_week** `int`  
       Percentage how much the peak maximum is above the mean busyness of the week.  
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
- **venue_info** `object`  
 Details of the forecasted venue.  
 &nbsp; 
  - venue_info.**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup. Note this name could be slightly different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_address** `string`  
   Address of the venue. This is the address of the venue as found by the geocoding lookup. Note this address could be different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_current_gmtttime** `string`  
   Time at the venue in Greenwich Mean Time. Adjusting the `hour_step` and `day_step` will also alter this time.  
 - venue_info.**venue_current_localtime_iso** `string`  
   Local time at the venue. Adjusting the `hour_step` and `day_step` will also alter this time.  
  &nbsp;
 - venue_info.**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is the primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.
  &nbsp;
 - venue_info.**venue_timezone** `string`  
   The timezone of the venue. E.g. `America/Los Angeles`  
  &nbsp;


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/peaks`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.



<!-- Content from _queryendpointsquiethours.md -->

# Query quiet hours

> Query quiet hours:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/quiet"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_step': 0,
    'hour_step':0
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/quiet?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&
day_step=0&
hour_step=0'
```

```javascript
const params = new URLSearchParams({ 
  'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
  'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
  'day_step': 0,
  'hour_step': 0
});

fetch(`https://besttime.app/api/v1/forecasts/quiet?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes Query Quiet hours

The 'query quiet hours' endpoint is used to retrieve all quiet hour information from an existing forecast for a specific day of the week.
By default, the response includes the quiet hour information for the current day (at the local timezone of the venue). 

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
 - **day_int** `int` <span style="color:blue">OPTIONAL</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday). `day_int` cannot be used in combination with `day_step` and `hour_step`.  
 &nbsp; 
- **day_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the day (day of week of the venue in the local timezone). E.g. `0` means current day, and `1` means tomorrow. Range: min `-31`, max `31`. `day_step` cannot be used in combination with `day_int`.  
 &nbsp;  
- **hour_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the hour (hour of the venue in the local timezone). E.g. `0` means current hour, and `-2` means two hours ago. Range: min `-12`, max `12`. `hour_step` cannot be used in combination with `day_int`.  
 &nbsp;
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Query quiet hours endpoint: https://besttime.app/api/v1/forecasts/quiet
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON response like this:

```json
{
    "analysis": {
        "day_info": {
            "day_int": 4,
            "day_rank_max": 7,
            "day_rank_mean": 3,
            "day_text": "Friday",
            "venue_closed": 4,
            "venue_open": 4
        },
        "quiet_hours": [
            {
                "quiet_end": 8,
                "quiet_end_12": "8AM",
                "quiet_end_in": "End of quiet period already passed",
                "quiet_end_in_sec": 0,
                "quiet_end_passed": 1,
                "quiet_period_duration": 2,
                "quiet_start": 6,
                "quiet_start_12": "6AM",
                "quiet_start_in": "Start of quiet period already passed",
                "quiet_start_in_sec": 0,
                "quiet_start_passed": 1
            },
            {
                "quiet_end": 6,
                "quiet_end_12": "6AM",
                "quiet_end_in": "18 hour and 7 minutes",
                "quiet_end_in_sec": 65280,
                "quiet_end_passed": 0,
                "quiet_period_duration": 3,
                "quiet_start": 3,
                "quiet_start_12": "3AM",
                "quiet_start_in": "15 hour and 7 minutes",
                "quiet_start_in_sec": 54480,
                "quiet_start_passed": 0
            }
        ],
        "quiet_hours_list": [
            6,
            7,
            3,
            4,
            5
        ],
        "quiet_hours_list_12h": [
            "6AM",
            "7AM",
            "3AM",
            "4AM",
            "5AM"
        ],
        "quiet_hours_list_coming": [
            3,
            4,
            5
        ],
        "quiet_hours_list_coming_12h": [
            "3AM",
            "4AM",
            "5AM"
        ]
    },
    "epoch_analysis": 1583911633,
    "forecast_updated_on": "2020-03-11T07:27:13.849228+00:00",
    "status": "OK",
    "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
    "venue_info": {
        "venue_current_gmttime": "Fri, 13 Mar 2020 18:52:28 GMT",
        "venue_current_localtime_iso": "2020-03-13T11:52:28.890102-07:00",
        "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles"
    },
    "venue_name": "McDonald's"
}
```

### Response attributes Query Quiet hours


- **analysis** `object`  
 Containing the all the quiet hour analysis and venue day info.
 - analysis.**quiet_hours** `list`  
   List with quiet hour objects, containing details of one or multiple quiet periods per day.  
  &nbsp;
     - analysis.quiet_hours.**quiet_start** `int`  
       Start hour of the quiet hour, using the 24 hour notation.  
       &nbsp;
     - analysis.quiet_hours.**quiet_start_passed** `int`  
       Indicates if the quiet hour start is already passed. Indicates `1` for passed, `0` for not passed.
       &nbsp;
     - analysis.quiet_hours.**quiet_start_12** `string`  
       Start hour of the quiet hour, using the 12 hour notation.  
       &nbsp;
     - analysis.quiet_hours.**quiet_start_in** `string`  
       Time remaining until the quiet hour starts. Notation 'HH hour and MM minutes'. If quiet hour start has been passed it will indicate `Start of quiet period already passed`  
       &nbsp;
     - analysis.quiet_hours.**quiet_start_in_sec** `int`  
       Time remaining until the quiet hour starts, in seconds.  
       &nbsp;
     - analysis.quiet_hours.**quiet_period_duration** `int`  
       Duration of the quiet period, in hours.  
       &nbsp;
     - analysis.quiet_hours.**quiet_end** `int`  
       End hour of the quiet hour, using the 24 hour notation.  
       &nbsp;
     - analysis.quiet_hours.**quiet_end_passed** `int`  
       Indicates if the quiet hour end is already passed. Indicates `1` for passed, `0` for not passed.
       &nbsp;
     - analysis.quiet_hours.**quiet_end_12** `string`  
       End hour of the quiet hour, using the 12 hour notation.  
       &nbsp;
     - analysis.quiet_hours.**quiet_end_in** `string`  
       Time remaining until the quiet hour ends. Notation 'HH hour and MM minutes'. If quiet hour end has been passed it will indicate `End of quiet period already passed`  
       &nbsp;
     - analysis.quiet_hours.**quiet_end_in_sec** `int`  
       Time remaining until the quiet hour ends, in seconds.  
       &nbsp;
 - analysis.**quiet_hours_list** `list`  
   List with quiet hours (`int`), in 24-hour notation.  
  &nbsp;
 - analysis.**quiet_hours_list_12h** `list`  
   List with quiet hours (`string`), in 12-hour notation.  
  &nbsp;
 - analysis.**quiet_hours_list_coming** `list`  
   List with quiet hours (`int`) which still have to come. In 24-hour notation.  
  &nbsp;
 - analysis.**quiet_hours_list_coming_12h** `list`  
   List with quiet hours (`string`) which still have to come, in 12-hour notation.  
  &nbsp;
- analysis.**day_info** `object`  
   Details about the day    
  &nbsp;
     - analysis.day_info.**day_int** `int`  
       Day integer range `0` (Monday) to `6` (Sunday)  
       &nbsp;
     - analysis.day_info.**day_rank_max** `int`  
       Day ranking based on the maximum quietness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most quiet day of the week.  
       &nbsp;
     - analysis.day_info.**day_rank_mean** `int`  
       Day ranking based on mean quietness (total volume) of the day. Range `1` to `7`. E.g. `7` indicates the least quiet day of the week.  
       &nbsp;
     - analysis.day_info.**day_text** `string`  
       Day name. E.g. `monday`  
       &nbsp;
     - analysis.day_info.**venue_closed** `int`/`string`  
       Hour of day when the venue closes. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.     
       &nbsp;
     - analysis.day_info.**venue_open** `int`/`string`  
       Hour of day when the venue opens. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.     
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
- **venue_info** `object`  
 Details of the forecasted venue.  
 &nbsp; 
  - venue_info.**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup. Note this name could be slightly different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_address** `string`  
   Address of the venue. This is the address of the venue as found by the geocoding lookup. Note this address could be different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_current_gmtttime** `string`  
   Time at the venue in Greenwich Mean Time. Adjusting the `hour_step` and `day_step` will also alter this time.  
 - venue_info.**venue_current_localtime_iso** `string`  
   Local time at the venue. Adjusting the `hour_step` and `day_step` will also alter this time.  
  &nbsp;
 - venue_info.**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is the primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.
  &nbsp;
 - venue_info.**venue_timezone** `string`  
   The timezone of the venue. E.g. `America/Los Angeles`  
  &nbsp;


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/quiet`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.



<!-- Content from _queryendpointsurge.md -->

# Query surge hours

> Query surge hours:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/surge"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
    'day_step': 0,
    'hour_step':0
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/surge?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843&
day_step=0&
hour_step=0'
```

```javascript
const params = new URLSearchParams({ 
  'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
  'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
  'day_step': 0,
  'hour_step': 0
});

fetch(`https://besttime.app/api/v1/forecasts/surge?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes Query surge hours

The 'query surge hours' endpoint is used to retrieve all surge hour information from an existing forecast for a specific day of the week.
By default, the response includes the surge hour information for the current day (at the local timezone of the venue). 

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
 - **day_int** `int` <span style="color:blue">OPTIONAL</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday). `day_int` cannot be used in combination with `day_step` and `hour_step`.  
 &nbsp; 
- **day_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the day (day of week of the venue in the local timezone). E.g. `0` means current day, and `1` means tomorrow. Range: min `-31`, max `31`. `day_step` cannot be used in combination with `day_int`.  
 &nbsp;  
- **hour_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the hour (hour of the venue in the local timezone). E.g. `0` means current hour, and `-2` means two hours ago. Range: min `-12`, max `12`. `hour_step` cannot be used in combination with `day_int`.  
 &nbsp;
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Query surge hours endpoint: https://besttime.app/api/v1/forecasts/surge
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON response like this:

```json
{
    "analysis": {
        "day_info": {
            "day_int": 0,
            "day_rank_max": 5,
            "day_rank_mean": 5,
            "day_text": "Monday",
            "venue_closed": 4,
            "venue_open": 4
        },
        "surge_hours": {
            "most_people_come": 8,
            "most_people_come_12h": "8AM",
            "most_people_come_passed": 0,
            "most_people_come_start_in": "Most people are coming in now",
            "most_people_come_start_in_sec": 0,
            "most_people_leave": 1,
            "most_people_leave_12h": "1AM",
            "most_people_leave_passed": 0,
            "most_people_leave_start_in": "16 hour and 26 minutes",
            "most_people_leave_start_in_sec": 59160
        }
    },
    "epoch_analysis": 1583911633,
    "forecast_updated_on": "2020-03-11T07:27:13.841800+00:00",
    "status": "OK",
    "venue_info": {
        "venue_current_gmttime": "Mon, 16 Mar 2020 15:34:59 GMT",
        "venue_current_localtime_iso": "2020-03-16T08:34:59.778538-07:00",
        "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles"
    },
    "venue_name": "McDonald's"
}
```

### Response attributes Query Surge hours


- **analysis** `object`  
 Containing the all the surge hour analysis and venue day info.
 - analysis.**surge_hours** `list`  
   List with surge hour objects, containing details of one or multiple surge periods per day.  
  &nbsp;
     - analysis.surge_hours.**surge_start** `int`  
       Start hour of the surge hour, using the 24 hour notation.  
       &nbsp;
     - analysis.surge_hours.**surge_start_passed** `int`  
       Indicates if the surge hour start is already passed. Indicates `1` for passed, `0` for not passed.
       &nbsp;
     - analysis.surge_hours.**surge_start_12** `string`  
       Start hour of the surge hour, using the 12 hour notation.  
       &nbsp;
     - analysis.surge_hours.**surge_start_in** `string`  
       Time remaining until the surge hour starts. Notation 'HH hour and MM minutes'. If surge hour start has been passed it will indicate `Start of surge period already passed`  
       &nbsp;
     - analysis.surge_hours.**surge_start_in_sec** `int`  
       Time remaining until the surge hour starts, in seconds.  
       &nbsp;
     - analysis.surge_hours.**surge_end** `int`  
       End hour of the surge hour, using the 24 hour notation.  
       &nbsp;
     - analysis.surge_hours.**surge_end_passed** `int`  
       Indicates if the surge hour end is already passed. Indicates `1` for passed, `0` for not passed.
       &nbsp;
     - analysis.surge_hours.**surge_end_12** `string`  
       End hour of the surge hour, using the 12 hour notation.  
       &nbsp;
     - analysis.surge_hours.**surge_end_in** `string`  
       Time remaining until the surge hour ends. Notation 'HH hour and MM minutes'. If surge hour end has been passed it will indicate `End of surge period already passed`  
       &nbsp;
     - analysis.surge_hours.**surge_end_in_sec** `int`  
       Time remaining until the surge hour ends, in seconds.  
       &nbsp;
 - analysis.**surge_hours_list** `list`  
   List with surge hours (`int`), in 24-hour notation.  
  &nbsp;
 - analysis.**surge_hours_list_12h** `list`  
   List with surge hours (`string`), in 12-hour notation.  
  &nbsp;
 - analysis.**surge_hours_list_coming** `list`  
   List with surge hours (`int`) which still have to come. In 24-hour notation.  
  &nbsp;
 - analysis.**surge_hours_list_coming_12h** `list`  
   List with surge hours (`string`) which still have to come, in 12-hour notation.  
  &nbsp;
- analysis.**day_info** `object`  
   Details about the day    
  &nbsp;
     - analysis.day_info.**day_int** `int`  
       Day integer range `0` (Monday) to `6` (Sunday)  
       &nbsp;
     - analysis.day_info.**day_rank_max** `int`  
       Day ranking based on the maximum busyness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most busy day of the week.  
       &nbsp;
     - analysis.day_info.**day_rank_mean** `int`  
       Day ranking based on mean busyness (total volume) of the day. Range `1` to `7`. E.g. `7` indicates the least busy day of the week.  
       &nbsp;
     - analysis.day_info.**day_text** `string`  
       Day name. E.g. `monday`  
       &nbsp;
     - analysis.day_info.**venue_closed** `int`/`string`  
       Hour of day when the venue closes. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.  
       &nbsp;
     - analysis.day_info.**venue_open** `int`/`string`  
       Hour of day when the venue opens. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.  
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
- **venue_info** `object`  
 Details of the forecasted venue.  
 &nbsp; 
  - venue_info.**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup. Note this name could be slightly different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_address** `string`  
   Address of the venue. This is the address of the venue as found by the geocoding lookup. Note this address could be different than the `venue_address` used as input.  
  &nbsp;
 - venue_info.**venue_current_gmtttime** `string`  
   Time at the venue in Greenwich Mean Time. Adjusting the `hour_step` and `day_step` will also alter this time.  
 - venue_info.**venue_current_localtime_iso** `string`  
   Local time at the venue.  
  &nbsp;
 - venue_info.**venue_id** `string`  
   Unique BestTime.app venue id. The `venue_id` is generated based on the venue name + address geocoding result. Therefore, when forecasting the same venue again it results in the same venue id. The `venue_id` is the primary input parameter to lookup (query) an existing forecast, using the [query endpoints] (#query-endpoints).
   The `venue_id` is used to perform queries.
  &nbsp;
 - venue_info.**venue_timezone** `string`  
  The timezone of the venue. E.g. `America/Los Angeles`  
  &nbsp;


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/surge`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.



<!-- Content from _queryendpointsvenue.md -->

# Query venue

> Query a single venue:

```python
import requests
 
url = "https://besttime.app/api/v1/venues/ven_51387131543761435650505241346a394a6432395362654a496843"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754'
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/venues/ven_51387131543761435650505241346a394a6432395362654a496843&
api_key_public=pub_e11661721b084d36b8f469a2c012e754'
```

```javascript
fetch(`https://besttime.app/api/v1/venues/ven_51387131543761435650505241346a394a6432395362654a496843?api_key_public=pub_e11661721b084d36b8f469a2c012e754`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes Query Venue

The 'query venue' endpoint is used to retrieve information about the venue. It does not contain forecasted data, except the day rankings for a week. This query endpoint requires the private API key. Although the private API keys is used, this endpoint will be charged with query credits.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 

- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Query venue endpoint: https://besttime.app/api/v1/venues/{{venue_id}}
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
        "venue_current_gmttime": "Friday 2021-04-23 07:26AM",
        "venue_current_localtime_iso": "Friday 2021-04-23 03:26PM",
        "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843",
        "venue_lat": 37.7235448,
        "venue_lng": -122.455458,
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles",
        "venue_dwell_time_min": 20,
        "venue_dwell_time_max": 20,
        "venue_type": "FAST_FOOD",
        "venue_types": [
            "fast_food_restaurant",
            "breakfast_restaurant",
            "coffee_shop",
            "hamburger_restaurant",
            "restaurant",
            "sandwich_shop"
        ],
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
   Local time at the venue.
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
- venue_info.**venue_dwell_time_min** `int`  
   Minimum usual visitor dwell time in minutes, or `0` when not available.  
  &nbsp;
 - venue_info.**venue_dwell_time_max** `int`  
   Maximum usual visitor dwell time in minutes, or `0` when not available.   
  &nbsp;
 - venue_info.**venue_dwell_time_avg** `int`  
   Average usual visitor dwell time in minutes, or `0` when not available.   
  &nbsp;
  - venue_info.**venue_type** `string`  
   Type of venue, or `OTHER` when not available. Possible types are (most common shown first) `RESTAURANT, SHOPPING, FAST_FOOD, BAR, SUPERMARKET, GROCERY, PARK, OTHER, APPAREL, FOOD_AND_DRINK, CAFE, SHOPPING_CENTER, COFFEE, AIRPORT, SPORTS_COMPLEX, PHARMACY, PERSONAL_CARE, VEHICLE, GAS_STATION, MUSEUM, DENTIST, LIBRARY, BANKING, TOURIST_DESTINATION, CASH_MACHINE, FOOD_DELIVERY, EVENT_VENUE, SPA, MARKET, CLUBS, PUBLIC_TRANSIT, BREWERY, SPORTING_GOODS, HISTORICAL, PERFORMING_ARTS, DOCTOR, AMUSEMENT_PARK, GIFTS, TEA, CHURCH, SKILL_INSTRUCTION, TRAIN_STATION, ARTS, GOLF, ZOO, BOTANICAL_GARDEN, NATIONAL_PARK, SUBWAY_STATION, CASINO, MOVIE_THEATER, POST_OFFICE, HIKING, GOLF_COURSE, NATURE_RESERVE, BRIDGE, BUS_STATION, GOVERNMENT, REST_AREA, WINERY, SCENIC_POINT, SOUVENIR_SHOP, CITY_HALL, BOATING, CONCERT_HALL, SWIMMING, MONUMENT, SOCCER, CAR_RENTAL, MOSQUE, INDUSTRIAL, VISITOR_CENTER, ANTIQUES, AQUARIUM, PALACE, HINDU_TEMPLE, STADIUM, WINTER_SPORTS, BUDDHIST_TEMPLE, EMBASSY, TEMPLE, TENNIS, BASEBALL, FERRY_TERMINAL, FISHING, POLICE, SCHOOL, BAKERY, AGRICULTURE, CRICKET, FAIRGROUNDS, GONDOLA_LIFT_STATION, HOSPITAL, LIGHTHOUSE, MILITARY, MORMON_TEMPLE, UNIVERSITY` 
  &nbsp;
- venue_info.**venue_types** `list`  
   Detailed venue types/services (not to confuse with `venue_type`)

### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/venues`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.

<!-- Content from _queryendpointsvenues.md -->

# Query all venues

> Query list of all forecasted venues:

```python
import requests
 
url = "https://besttime.app/api/v1/venues"

params = {
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b'
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/venues?
api_key_private=pri_50990bf1f8828f6abbf6152013113c6b'
```

```javascript
fetch(`https://besttime.app/api/v1/venues?api_key_private=pri_50990bf1f8828f6abbf6152013113c6b`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes Query All Venues

The 'query venues' endpoint is used to retrieve a list with all previously forecasted venues. This query endpoint requires the private API key. Although the private API keys is used, this endpoint will be charged with query credits.

- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
   Private API Key. See more info on [API keys](#api-reference)  
 &nbsp; 
- **limit** `int` <span style="color:blue">OPTIONAL</span>    
   Maximum number returned venues. Default `1000`, min `0`, max `10000`.  
  &nbsp; 
- **page** `int` <span style="color:blue">OPTIONAL</span>    
   Selects the page number. Default page `0`. Min page `0`.  
  &nbsp; 

<aside class="notice">
Query venues endpoint: https://besttime.app/api/v1/venues
</aside>

<aside class="notice">
HTTP method: GET
</aside>

<aside class="warning">
API Credit usage per API call for this endpoint depends on the number of returned venues and your plan. See 'API key credits' for more information.
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
 - venue[N].**forecast_updated_on** `DateTime string`  
   Date and time of the last foot traffic forecast in UTC.



<!-- Content from _queryendpointsvenuesfilter.md -->

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
    'types': 'BAR,CAFE,RESTAURANT',
    'lat': 51.5121172,
    'lng': -0.126173,
    'radius': 2000,
    'order_by': 'day_rank_max,reviews',
    'order': 'desc,desc',
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
    'types': 'BAR,CAFE,RESTAURANT',
    'lat': 51.5121172,
    'lng': -0.126173,
    'radius': 2000,
    'order_by': 'day_rank_max,reviews',
    'order': 'desc,desc',
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

The 'venue filter' endpoint will return all venues and foot traffic data that meet the filter requirements. Venues can be filtered on how busy they are, on  location, type of venue, day & time range, etc, or a combination. This could be useful to for e.g. find all busy bars, cafes and nightclubs, between 6pm and 11pm in a specific neighborhood. 

The BestTime Radar tool is using the same API endpoint to show all venues that meet the filter criteria on a (heat)map.

By default (for new users after July 25 2024) the venue filter will return all venues meeting the filter criteria in the BestTime database. Older users see by default only venues that have been previously added by this account (specifically this API key set). Behavior can be changed using the `own_venues_only` parameter.

If venues are missing you can add them individually using the New Foot Traffic Forecast API, or multiple venues using the Venue Search API.

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
 Selects which part(s) of the foot traffic data will be returned. Can be `limited`, `day`, or `both`. Default is `limited`. With `limited` selected, only the foot traffic data between the selected hours (`hour_min` and `hour_max`) is returned in the `day_raw` value result (or whole day when no hours are selected). This also applies when combining with `now`  in the input. When `day` is selected, foot traffic data for the whole day is returned (regardless of the filtered hours) in the `day_raw_whole` value result. The `day_raw` value is in this case not returned. When `both` is selected, both the previously described `day_raw` and `day_raw_whole` value results are returned in the response.
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
 Will display the live foot traffic data. Venues without live data will be filtered out. Note: The Venue Filter does NOT refresh the live data automatically. Use the Live API endpoint to refresh the data for example every hour. The local time of the first venue is taken that matches the filter criteria. Cannot be used in combination with the `now`, `day_int`, `hour_min`, and `hour_max` parameters. 
 &nbsp;
<!-- - **live_refresh** `bool` <span style="color:blue">OPTIONAL</span>
 Live_refresh set to `true` will refresh all live and forecast data (new venue Foot Traffic Forecast) for each individual venue meeting the filter. This will slow down the request and results in extra API credits per refreshed venue. By default set to `false` to get a faster response and lower API credit usage. Note: The live_refresh will ignore the `limit` parameter to refresh all venues matching the other parameters. Only after the refresh the venue limit is applied. This may result in high API credit usage. Use the New Forecast or Live endpoints to manually control which venues needs to be updated.
 &nbsp;
 - **live_limit** `int` <span style="color:blue">OPTIONAL</span>
Limits the maximum number of venues refreshed when `live` and `live_refresh` is set to `true`. Default `500`, min `0`, max `5000`.
 &nbsp; -->
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
- **own_venues_only** `int` <span style="color:blue">OPTIONAL</span>
  Optionally only return venues that have previously been added to your account or filtered instead of all venues available on BestTime. Default `false` for users after July 25 2024. Users before this date need to manually set this parameter to `false` to return all available venues from BestTime that meet the filter criteria. Note: If venues are missing you can try to add them using a New Foot Traffic Forecast API call or the Venue Search API.
  &nbsp;

- **order_by** `int` <span style="color:blue">OPTIONAL</span>
   BETA: Sort venues on foot traffic intensity data. Order venues by a specific parameter. Can be `reviews`,`rating`,`price_level`,`now`,`name`,`day_rank_max`,`day_rank_mean`,`day_max`,`day_mean`,`date`, `dwell_time_min`,`dwell_time_max`,`0`,`1`,`2`,`3`,`4`,`5`,`6`,`7`,`8`,`9`,`10`,`11`,`12`,`13`,`13`,`14`,`15`,`16`,`17`,`18`,`19`,`20`,`21`,`22`,`23`. Default is `reviews`. Max two comma separated parameters allowed (e.g. `order_by=rating,reviews`). The 24 numbers represent the foot traffic data for each of the 24 hours in a day. E.g. `16` will sort the venues based on predicted foot traffic at 16:00 (4PM). Warning: Venues forecasted before July 1st, 2021 need to be updated (new foot traffic forecast) to order them correctly.
  &nbsp;
- **order** `int` <span style="color:blue">OPTIONAL</span>
   Order the `order_by` parameters ascending or descending. Can be `asc` or `desc`.  Default `desc`. Max two comma seperated parameters allowed (e.g. `order=desc,asc`).
  &nbsp;
- **limit** `int` <span style="color:blue">OPTIONAL</span>
   Maximum number returned venues. Default `5000`, min `0`, max `10000`. Higher limits result in slower responses and higher API credit usage. 
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
      "day_info": {
          "day_int": 4,
          "day_max": 74,
          "day_mean": 55,
          "day_rank_max": 7,
          "day_rank_mean": 4,
          "day_text": "Friday",
          "venue_closed": 22,
          "venue_open": 7
      },
      "day_int": 4,
      "day_raw": [
          65,
          65,
          60,
          50,
          0,
          0
      ],
      "day_raw_whole": [
          0,
          10,
          35,
          50,
          45,
          55,
          70,
          75,
          70,
          60,
          60,
          60,
          65,
          65,
          60,
          50,
          0,
          0,
          0,
          0,
          0,
          0,
          0,
          0
      ],
      "price_level": 0,
      "rating": 4.6,
      "reviews": 496,
      "venue_address": "45 Jermyn St St. James's, London SW1Y 6DN United Kingdom",
      "venue_dwell_time_max": 120,
      "venue_dwell_time_min": 60,
      "venue_id": "ven_6f39545031476b54345f5852676b6445596457484a79674a496843",
      "venue_lat": 51.5080107,
      "venue_lng": -0.1382948,
      "venue_name": "45 Jermyn St.",
      "venue_type": "RESTAURANT"
    },
    {
      "day_info": {
          "day_int": 4,
          "day_max": 87,
          "day_mean": 41,
          "day_rank_max": 2,
          "day_rank_mean": 3,
          "day_text": "Friday",
          "venue_closed": 0,
          "venue_open": 12
      },
      "day_int": 4,
      "day_raw": [
          55,
          80,
          85,
          80,
          55,
          30
      ],
      "day_raw_whole": [
          0,
          0,
          0,
          0,
          0,
          0,
          15,
          20,
          15,
          10,
          15,
          30,
          55,
          80,
          85,
          80,
          55,
          30,
          15,
          0,
          0,
          0,
          0,
          0
      ],
      "price_level": 2,
      "rating": 4.5,
      "reviews": 1782,
      "venue_address": "7 Northumberland Ave London WC2N 5BY United Kingdom",
      "venue_dwell_time_max": 120,
      "venue_dwell_time_min": 60,
      "venue_id": "ven_6f5a30484241302d48623552676b6446556e49492d36374a496843",
      "venue_lat": 51.5071129,
      "venue_lng": -0.1265196,
      "venue_name": "50 Kalò di Ciro Salvo Pizzeria London",
      "venue_type": "RESTAURANT"
    }
  ],
  "venues_n": 2,
  "window": {
      "day_window": "Friday 6PM until Friday 11PM",
      "day_window_end_int": 4,
      "day_window_end_txt": "Friday",
      "day_window_start_int": 4,
      "day_window_start_txt": "Friday",
      "time_local": 8,
      "time_local_12": "8AM",
      "time_local_index": 2,
      "time_window_end": 23,
      "time_window_end_12h": "11PM",
      "time_window_end_ix": 17,
      "time_window_start": 18,
      "time_window_start_12h": "6PM",
      "time_window_start_ix": 12
  }
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
  &nbsp;
 - venues[N].**day_info** `object`
   Details about the day.
  &nbsp;
     - venues[N].day_info.**day_int** `int`
       Day integer range `0` (Monday) to `6` (Sunday)
       &nbsp;
     - venues[N].day_info.**day_rank_max** `int`
       Day ranking based on maximum busyness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most busy day of the week.
       &nbsp;
     - venues[N].day_info.**day_rank_mean** `int`
       Day ranking based on mean busyness (total volume) of the day. Range `1` to `7`. E.g. `7` indicates the least busy day of the week.
       &nbsp;
     - venues[N].day_info.**day_text** `string`
       Day name. E.g. `monday`
       &nbsp;
     - venues[N].day_info.**venue_closed** `int`/`string`
       Hour of day when the venue closes. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.
       &nbsp;
     - venues[N].day_info.**venue_open** `int`/`string`
       Hour of day when the venue opens. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.
       &nbsp;

- **window** `object`
  Indicating the time window of the foot traffic data. See Introduction section [Forecast day window and weekdays](#forecast-day-window-and-weekdays)
  &nbsp;
  - window.**day_window** `string`
    Time window of the foot traffic data as a human readable sentence.
  &nbsp;
  - window.**day_window_end_int** `int`
    Week day (day_int) of the window end. Range `0` to `6`.
  &nbsp;
  - window.**day_window_end_txt** `string`
    Week day as text of the window end.
  &nbsp;
  - window.**day_window_start_int** `int`
    Week day (day_int) of the window start. Range `0` to `6`.
  &nbsp;
  - window.**day_window_start_txt** `string`
    Week day as text of the window start.
  &nbsp;
  - window.**time_local** `int`
    Current local hour of day at location in 24 hour format. Range `0` to `23` hour.
  &nbsp;
  - window.**time_local_12** `string`
    Current local hour of day at location in 12 hour format. Range `12AM` to `23PM` hour.
  &nbsp;
  - window.**time_local_index** `int`
    The index value of the element in a 24 hour foot traffic data array corresponding to the foot traffic data for the current local hour. In the example, the value is `2`. If no hour_min and hour_max filter is applied the `day_raw` array will consist of 24 elements. However, in the example, the hours are filtered and the `day_raw` array only consists out of six elements. In this example, the `foot_traffic` input is set to `both` so it will also return a full 24 element foot traffic array in the `day_raw_whole`. So the `time_local_index=2` corresponds to a foot traffic percentage of `35` in the second venue in the example response (45 Jermyn St.). As alternative, to get both the foot traffic value for the current hour and the whole 24 hour foot traffic array - it is recommended to set `now=true` and `foot_traffic` to both. The `day_raw` with one element will then indicate the foot traffic percentage currently at each venue.
  &nbsp;
  - window.**time_window_end** `int`
    Hour of the window end. Range `0` to `23` hour.
  &nbsp;
  - window.**time_window_end_12** `string`
    Hour of the window end. Range `12AM` to `23PM` hour.
  &nbsp;
  - window.**time_window_end_ix** `int`
    The index value of the element in a 24 hour foot traffic data array corresponding to last hour of the window.
  &nbsp;
  - window.**time_window_start** `int`
    Hour of the window start. Range `0` to `23` hour.
  &nbsp;
  - window.**time_window_start_12** `string`
    Hour of the window start. Range `12AM` to `23PM` hour.
  &nbsp;
  - window.**time_window_start_ix** `int`
    The index value of the element in a 24 hour foot traffic data array corresponding to first hour of the window.
  &nbsp;

- venues_n `int`
  The total number of found venues. Please add venues first to your account before using the Venue Filter tool. You can add venues using the New Foot Traffic Forecast tool/ API to individually add venues, or using the Venue Search tool/ API to add multiple venues at once. Remove filters to increase the amount of returned venues.


<!-- Content from _queryendpointsvenuessearch.md -->

# Venue Search 

> Find and add new venues based on a search query.

```python
import requests

url = "https://besttime.app/api/v1/venues/search"

params = {
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
    'q': 'supermarkets in sydney australia',
    'num': 200,
    'fast': False,
    'format': 'raw'
}

response = requests.request("POST", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request POST 'https://besttime.app/api/v1/venues/search?api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&q=quiet%20supermarkets%20in%20sydney%20australia%20sunday%20morning&num=200&fast=false&format=raw'
```

```javascript
const params = new URLSearchParams({ 
    'api_key_private': 'pri_50990bf1f8828f6abbf6152013113c6b',
    'q': 'supermarkets in sydney australia',
    'num': 200,
    'fast': false,
    'format': 'raw'
});

fetch(`https://besttime.app/api/v1/venues/search?${params}`, {
  method: 'POST'
}).then(function(data) { 
  console.log(data); 
});
```

Find and add multiple new venues based on a search query. The search query can e.g. contain the name of a venue (e.g. McDonald's, Walmart,etc), or a type of venue (e.g. supermarkets, pizza, beach, things to do, etc). 

The search query can be narrowed down with additional filters like the location (e.g. a neighborhood, city, or country), or add geographical data (lat, lng, radius) to find venues related to the search query in a geographic location.

Note: Use the 'New foot traffic forecast' API endpoint when searching for a single venue (this is much faster).

Multiple API endpoints are involved from entering a search input until returning foot-traffic data for the found venues.
The Venue Search model will lookup venues in the background and will forecast them subsequently. Remember that this will therefore also result in forecast API credit usage. The endpoint will reply with a background task URL, `job_id`, and a `collection_id` (see [Collections](#venue-collections)).  You can poll the Venue Search Progress endpoint to poll to progress. The venue search functionality can also be used without API using the website [Venue Search Tool](https://besttime.app/api/v1/searchvenues) or on the [Radar tool](https://besttime.app/api/v1/radar/filter).

Once finished and if available for the venue, the Venue Search Progress endpoint will return the foot traffic data for the found venues. This data is similar to the `day_info` and `day_raw` response values of the [New Foot Traffic Forecast](#input-attributes-new-forecast) endpoint. However, it does not include all additional analyses. Use the [Query Week](#query-week) endpoint to get the whole forecast analysis using the venue_id. Normally API credits are charged for this endpoint, but is free within one day after created a new forecast (through the Venue Search- or directly through the [New Foot Traffic Forecast](#input-attributes-new-forecast) endpoint).

<b>Highly recommended to read first:
- [BestTime tools beginners tutorial](https://blog.besttime.app/foot-traffic-nightlife-bars/)
- [BestTime Software API beginners tutorial](https://blog.besttime.app/beginners-guide-foot-traffic-data-software-api/)
</b>

This query endpoint requires the private API key. 

### Input attributes Venue Search

- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. The endpoint will only return venues that are forecasted with this private API key. See [API keys](#api-reference) for more info.
 &nbsp;
- **q** `string` <span style="color:orange">REQUIRED</span>  
 Text query to search venues with a matching venue name (e.g. Whole Foods), or venue type (e.g. restaurants), and location (e.g. neighborhood, city, state or country). Max length `128` characters. You can use natural language to automatically add venue filters. See [Natural Language in a search query](#natural-language-in-the-search-query-as-filters)
 &nbsp;
- **num** `int` <span style="color:blue">OPTIONAL</span>  
Maximum number of search results, with increments of 20 venues, and a range from `20` to `200`.
The default number is `20`. API credits for this endpoint are counted per `20` search results. The search time grows linearly with the number of requested numbers (see also parameter `fast`).    
&nbsp;
- **format** `string` <span style="color:blue">OPTIONAL</span>  
Format for the foot traffic forecast of `venue_foot_traffic_forecast` returned in the final search results (if the venue has foot traffic data available). Choices are: `none, raw, all`. Choosing `raw` will only return the hourly foot traffic percentages for every day of the week (default). `all` will return the raw data including all foot traffic analyses, similar to the 'New Foot Traffic Forecast' and 'Query Week' response format. Select `None` skip the foot traffic data in the response to reduce the response size and increase the performance (e.g. if you use the foot traffic filter endpoint after this).   
 &nbsp;
- **opened** `string` <span style="color:blue">OPTIONAL</span>  
Search for venues with specific opening times. Options are `24`, `now`, `all` . `24` will return venues with a 24 hour opening time. `now` will return venues that are opened at this moment. `all` will return all venues regardless of their opening hours. Defaults to `all`.
 &nbsp;
- **fast** `boolean` <span style="color:blue">OPTIONAL</span>  
Boolean to select the normal speed or fast search method. Searching with the fast method is charged with more API credits. Defaults to `true` (fast search speed). The fast method is limited to a maximum `num` of `60`. Selecting a higher number will automatically use the normal speed method. Select `false` to save on API credits or to search for more venues. See [API Credits](#credits) for more info. Fixed packages each have a limited number of fast and normal search queries per month. The Pro - metered plan has a limit of 10000 fast venue search calls per calendar month. Contact us for high-volume fast or normal search queries.
 &nbsp;

- **collection_id** `string` <span style="color:blue">OPTIONAL</span>  
Add the results to an existing or user-defined collection_id. If this parameter is omitted a new unique collection_id will be generated. All successfully forecasted venues will be automatically added to this collection. By giving an existing collection_id the user can merge the new venues with an existing venue collection. See [Collections](#collections) for more info.
 &nbsp;

- **lat** `float` <span style="color:blue">OPTIONAL</span>  
   Geographic latitude of the search circle. A maximum of 3 decimal floating points are allowed (≈ 111 meter). This will be enforced starting from September 1st, 2021.  `lat` must be combined with `lng`, and `radius`. The search circle cannot be combined with the bounding box parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp;
- **lng** `float` <span style="color:blue">OPTIONAL</span>  
   Geographic longitude of the search circle. A maximum of 3 decimal floating points are allowed (≈ 111 meter). This will be enforced starting from September 1st, 2021.  `lng` must be combined with `lat`, and `radius`. The search circle cannot be combined with the bounding box parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp; 
- **radius** `int` <span style="color:blue">OPTIONAL</span>  
   Radius of the search circle in meter.  `radius` must be combined with `lat`, and `lng`. The search circle cannot be combined with the bounding box parameters. Either a combination of a `lat`, `lng`, with a `radius` or `lat_min`, `lng_min`, `lat_max`, and `lng_max` is required.  
  &nbsp;   
- **live** `bool` <span style="color:blue">OPTIONAL</span>    
 The live attribute value changes the behavior of both the Venue Search and optionally the subsequent Venue Filter response. Venue Search: When `live=true`, the Venue Search will always refresh the data and Search Progress response will contains live data (if available). When `format=raw` it will only include the raw live percentage in `venue_foot_traffic_live`. When `format=all` the response includes the live data - including the analysis similar to the [Live foot-traffic data](#live-foot-traffic-data) endpoint) - in `venue_foot_traffic_live`.
 Venue Filter: Sets the time and day filter to the current day and hour in local time, and will display the live busyness. Venues without live data will be filtered out. The local time of the first venue is taken that matches the filter criteria. Cannot be used in combination with the `now`, `day_int`, `hour_min`, and `hour_max` parameters.  
 &nbsp; 


<aside class="notice">
Search venue endpoint: https://besttime.app/api/v1/venues/search
</aside>

<aside class="notice">
HTTP method: POST
</aside>

<aside class="warning">
API Credit usage per API call for this endpoint depends on the number `num` of requested venues and the search speed (Normal or Fast). See 'API key credits' for more information.
</aside>


<aside class="warning">
The Venue Search endpoint is by default limited to 30 requests per minute, and 300 requests per hour. Contact us for higher limits.
</aside>


> The above request returns a JSON response with links to the background job:

```json
{
    "_links": {
        "venue_search_progress": "https://besttime.app/api/v1/venues/progress?job_id=e0880f28-3a19-4871-a355-4ca21f10c2c8&collection_id=col_ac734e76ad2d4696a5a66541c67587e8&format=raw"
    },
    "collection_id": "col_ac734e76ad2d4696a5a66541c67587e8",
    "job_id": "e0880f28-3a19-4871-a355-4ca21f10c2c8",
    "status": "OK"
}
```


### Response attributes Venue Search
The JSON response will contain a URL to the Venue Search Progress endpoint to track the progress of the current venue search that runs in the background. This URL is the same as the [Venue Search Progress](#response-attributes-venue-search) API endpoint.

- **_links** `object` 
  &nbsp;
  - _links.**venue_search_progress** `string`  
    Link to the venue search background job. Use this link to check the progress on the search venues query. When the job is finished it will display the found venues, how many venues have forecast data, and links to show the found venues with foot-traffic results directly in the 'Radar tool` and 'venue filter' endpoints. For more info see [Venue Search Progress](#response-attributes-venue-search).
    &nbsp;
    
    &nbsp;
- **collection_id** `string` 
 Unique ID for the collection, 36 characters long. See [Collections](#venue-collections). 
 - **job_id** `string` 
 Unique ID for the venue search background job.  
- **status** `string` 
 Status of the response. Either `OK` or `error`.


## Venue Search Progress

> Venue Search Progress endpoint

```python
import requests

url = "https://besttime.app/api/v1/venues/progress"

params = {
    'job_id': '0a693bb3-7bd6-4d43-9495-a2773f1c9e29',
    'collection_id': 'col_ffbebb4003974979b75a14844d60e9c5',
    'format': 'raw'
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/venues/progress?
job_id=0a693bb3-7bd6-4d43-9495-a2773f1c9e29&collection_id=col_ffbebb4003974979b75a14844d60e9c5&
format=raw'
```

```javascript
const params = new URLSearchParams({ 
    'job_id': '0a693bb3-7bd6-4d43-9495-a2773f1c9e29',
    'collection_id': 'col_ffbebb4003974979b75a14844d60e9c5',
    'format': 'raw'
});

fetch(`https://besttime.app/api/v1/venues/progress?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes Venue Search Progress

- **job_id** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. The endpoint will only return venues that are forecasted with this private API key. See [API keys](#api-reference) for more info.
 &nbsp;
- **collection_id** `string` <span style="color:blue">OPTIONAL</span>  
Adding the `collection_id` passes on the collection_id in the result links once the venue search is finished. See [Collections](#venue-collections).  
 &nbsp;


> The above request returns a JSON response with the progress of the venue search. Once it is complete it will show the second displayed JSON response.

```json
{
    "collection_id": "col_5c546908473645c1b9bad36b7fef7765",
    "count_completed": 140,
    "count_failure": 0,
    "count_forecast": 129,
    "count_live": 74,
    "count_total": 200,
    "job_finished": false,
    "job_id": "eb6aa504-e147-4b2d-a191-03d721764279",
    "status": "OK"
}
```


> When the venue search is complete it will return a JSON response with the following structure :

```json
{
    "_links": {
        "background_progress_api": "http://besttime.app/api/v1/venues/progress?job_id=eb6aa504-e147-4b2d-a191-03d721764279&ven=False",
        "background_progress_tool": "http://besttime.app/api/v1/misc/addarea_progress?q=quiet+supermarkets+in+sydney+australia+sunday+morning&job_id=eb6aa504-e147-4b2d-a191-03d721764279&map_lat=-33.8627418&map_lng=151.2165809&lat_min=-33.8877752&lat_max=-33.8377084&lng_min=151.1962989&lng_max=151.2368629&map_zoom=14&radius=6712&collection_id=col_5c546908473645c1b9bad36b7fef7765&api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&busy_min=0&busy_max=50&day_int=6&hour_min=6&hour_max=11&now=True&live_refresh=False&auto_continue=1",
        "radar_tool": "http://besttime.app/api/v1/radar/filter?q=quiet+supermarkets+in+sydney+australia+sunday+morning&map_lat=-33.8627418&map_lng=151.2165809&lat_min=-33.8877752&lat_max=-33.8377084&lng_min=151.1962989&lng_max=151.2368629&map_z=14&collection_id=col_5c546908473645c1b9bad36b7fef7765&api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&busy_min=0&busy_max=50&day_int=6&hour_min=6&hour_max=11&now=True&live_refresh=False",
        "venue_filter_api": "http://besttime.app/api/v1/venues/filter?lat_min=-33.8877752&lat_max=-33.8377084&lng_min=151.1962989&lng_max=151.2368629&collection_id=col_5c546908473645c1b9bad36b7fef7765&api_key_private=pri_50990bf1f8828f6abbf6152013113c6b&busy_min=0&busy_max=50&day_int=6&hour_min=6&hour_max=11&now=True&live_refresh=False"
    },
    "bounding_box": {
        "lat": -33.8627418,
        "lat_max": -33.8377084,
        "lat_min": -33.8877752,
        "lng": 151.2165809,
        "lng_max": 151.2368629,
        "lng_min": 151.1962989,
        "map_zoom": 14,
        "radius": 6712
    },
    "collection_id": "col_5c546908473645c1b9bad36b7fef7765",
    "count_completed": 200,
    "count_failure": 0,
    "count_forecast": 181,
    "count_live": 90,
    "count_total": 200,
    "job_finished": true,
    "job_id": "eb6aa504-e147-4b2d-a191-03d721764279",
    "status": "OK",
    "venues": [
        {
            "forecast": false,
            "processed": true,
            "venue_address": "21 Shelley St, Sydney NSW 2000, Australia",
            "venue_lat": -33.8670477,
            "venue_lon": 151.2023238,
            "venue_name": "Kings Wharf Supermarket",
            "venue_id": "ven_6372542d36476a8759686d52676b646155646e713661514a496843"
        },
        {
            "forecast": true,
            "processed": true,
            "venue_address": "4/490 Crown St, Surry Hills NSW 2010, Australia",
            "venue_lat": -33.8866095,
            "venue_lon": 151.2138922,
            "venue_name": "Maloneys Grocer",
            "venue_id": "ven_9372542d36476a8759686d52676b646155646e713661514a496847",
            "venue_foot_traffic_forecast": [
                {
                    "day_info": {
                        "day_int": 0,
                        "day_max": 25,
                        "day_mean": 12,
                        "day_rank_max": 6,
                        "day_rank_mean": 7,
                        "day_text": "Monday",
                        "venue_closed": 21,
                        "venue_open": 6
                    },
                    "day_int": 0,
                    "day_raw": [
                        5,
                        5,
                        5,
                        10,
                        15,
                        20,
                        20,
                        25,
                        25,
                        20,
                        15,
                        10,
                        5,
                        5,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0,
                        0
                    ]
                },
                {
                    "day_info": {
                        "day_int": 1,
                        "day_max": 24,
                        "day_mean": 12,
                        "day_rank_max": 7,
                        "day_rank_mean": 7,
                        "day_text": "Tuesday",
                        "venue_closed": 21,
                        "venue_open": 6
                    },
                    "day_int": 1,
                    "day_raw": [
                        0,
                        5,
                        5,
                        10,
                        15,
                        ...
        },
        ... Only the first two results are displayed here
    ],
    "venues_n": 200
}
```


### Response attributes Venue Search Progress
The JSON response will contain the progress of the Venue Search query and once completed it will return the remaining attributes as shown in the second part of the attributes below.

- **count_total** `int` 
 Total number of found venues matching the search query. When the venue search is still not finished (`job_finished: false`) this number could still go up until the maximum `num` of requested venues.  This number could also be below the number of requested venues, if there are no more matching venues are found.
- **count_completed** `int` 
 Number of venues processed (forecasted) in the background. 
- **count_forecasted** `int` 
 Number of venues with foot-traffic data (forecast data).  
- **count_live** `int` 
 Number of venues with live foot-traffic data.  
- **count_failed** `int` 
 Number of failed venues that resulted in errors. This number does not include venues without forecast data.  
- **job_finished** `bool` 
 Boolean indicating if the Venue Search has been completed. `true` or `false`.  
- **collection_id** `string` 
Unique ID for the collection, 36 characters long.  
- **job_id** `string` 
Unique ID for the venue search background job.  
- **status** `string` 
 Status of the response. Either `OK` or `error`.

The attributes below will be displayed when the Venue Search job is finished (`job_finished: true`).


- **_links** `object` 
  &nbsp;
  - _links.**radar_tool** `string`  
    URL to show the current Venue Search query results in the radar tool. The URL includes all relevant filters (both the manually applied filters and the filters triggered by the natural language filter detection functionality). 
    &nbsp;
  - _links.**venue_filter_api** `string`  
    URL to show the current Venue Search query results in the Venue Filter API endpoint. The URL includes all relevant filters (both the manually applied filters and the filters triggered by the natural language filter detection functionality).  
    &nbsp;
    &nbsp;

- **venues** `list` 
  List of venues meeting the Venue Search query without filters (busyness, day, time, etc). 
  &nbsp;
  - venues[N].**forecast** `bool`  
    Indicates if the venue has foot-traffic forecast data. `true` or `false`. 
    &nbsp;
  - venues[N].**processed** `bool`  
    Indicates if the venue has been processed (analyzed) for foot-traffic data. `true` or `false`. 
    &nbsp;
  - venues[N].**venue_address** `string`  
   Address of the venue. This is the address of the venue as found by the geocoding lookup. Note this address could be different than the `venue_address` used as input.  
    &nbsp; 
  - venues[N].**venue_name** `string`  
   Name of the venue. This is the name of the venue as found by the geocoding lookup. Note this name could be slightly different than the `venue_address` used as input.  
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
  - venues[N].**venue_foot_traffic_forecast** `string`  
   Foot-traffic forecast data for each hour of the day, for every day of the week. See [New Foot Traffic Forecast](#input-attributes-new-forecast) for details on the `day_info` and `day_raw` attributes. 
   
    Alternatively, use the [Query Week](#query-week) endpoint to get the whole forecast analysis using the venue_id. Normally API credits are charged for this endpoint, but is free within one day after created a new forecast (through the Venue Search- or directly through the [New Foot Traffic Forecast](#input-attributes-new-forecast) endpoint).     
   &nbsp;


   
- **venues_n** `int`
Total number of venues in list `venues`.
- **bounding_box** `object` 
  Geographical bounding box coordinates that fits all venues. Useful to for displaying venues on a map. As an alternative the map center lat, lng, map_zoom and a radius parameters are provided to view all results on a map.
  &nbsp;
  - bounding_box.**lat** `string`  
    Geographic map latitude center of venue search result.  
    &nbsp;
  - bounding_box.**lat_max** `string`  
    Maximum latitude of the bounding box (North-East). 
    &nbsp;
  - bounding_box.**lat_min** `string`  
    TOTO 
    &nbsp;
  - bounding_box.**lng** `string`  
    Geographic map longitude center of venue search result.   
    &nbsp;
  - bounding_box.**lng_max** `string`  
    Maximum longitude of the bounding box (North-East). 
    &nbsp;
  - bounding_box.**lng_min** `string`  
    Minimum longitude of the bounding box (South-West). 
    &nbsp;
  - bounding_box.**map_zoom** `string`  
    Recommended map_zoom value to make all found venues show on a map in combination with the provided `lat`, `lng` map center coordinates. 
    &nbsp;
  - bounding_box.**radius** `string`  
    Radius in meters of the venue search results. 
    &nbsp;



<!-- Content from _queryendpointsvenuesupdate.md -->

# Venues Update

> Show a list of venues that are older than a specified amount of weeks. Optionally update each listed venue with a 'new foot traffic forecast':

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

The 'Venues Update' endpoint returns a list of venues that are older than a specified amount of weeks for the given 'api_key_private'. Optionally update each listed venue with a 'new foot traffic forecast'. This endpoint can also be filtered by collection_id or a geographical bounding box. This is useful since venue foot traffic is only updated through a new 'New foot traffic forecast' per venue or venues from the  'Venue Search' results. The Venue Filter (except for live data) endpoint and other query endpoints will not update the foot traffic data.

- **api_key_private** `string` <span style="color:orange">REQUIRED</span>
 Private API Key. See more info on [API keys](#api-reference)
 &nbsp;
- **weeks** `int` <span style="color:blue">OPTIONAL</span>
 Return only venues that have not been updated more than the selected number of `weeks`. Default is `2`. Minimum is `0` and will return all matching venues regardless of the last update date.
 &nbsp;
- **update** `bool` <span style="color:blue">OPTIONAL</span>
  Automatically update all returned venues by pushing them to the 'New foot traffic forecast' API endpoint (normal API credits apply for each venue). Default is `false` (not updating).
 &nbsp;
- **foottraffic** `string` <span style="color:blue">OPTIONAL</span>
  Returns only venues with or without foot traffic data. Options `with`, `without`, `all`. `with` will return only venues that had foot traffic forecast data last update. `without` will only return venues that did not have foot traffic forecast data last update. `all` will return all matching venues regardless if they have foot traffic data. Default is `all`. Not all venues that have been added to your BestTime account have foot traffic data. Also, venues without foot traffic data will be stored in your account. By default, these venues will not be shown and updated to save API credits (`with`). Sometimes it can be useful to also update previously failed forecast - when e.g. venues are re-opened or are getting more popular (and therefore might have foot traffic at this moment).
 &nbsp;
- **collection_id** `string` <span style="color:blue">OPTIONAL</span>
Return only venues within an existing collection. See more info on [Collections](#venue-collections)
 &nbsp;
- **collection_ids** `comma separated list of strings` <span style="color:blue">OPTIONAL</span>
Return only venues from multiple collections. Add the collection ids separated by commas. By adding venues to multiple own defined collections (e.g. live-music, karaoke) you can use collection as tags. See more info on [Collections](#venue-collections)
 &nbsp;


Return only venues without a geographic bounding box:
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



<!-- Content from _queryendpointsweek.md -->

# Query week

> Query the week (whole forecast):

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/week"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/week?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843'
```

```javascript
const params = new URLSearchParams({ 
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
});

fetch(`https://besttime.app/api/v1/forecasts/week?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

> The above request returns a JSON structured similar as the [new forecast](#new-forecast) endpoint

> Click <a href="https://github.com/besttime-app/slate/blob/master/source/examples/forecast_new/forecast_new_response.json" target="_blank">here</a> for the full JSON response

### Input attributes

The 'query week' endpoint is used to retrieve all data from an existing forecast (every day of the week). The response structure is exactly the same as the [new forecast](#new-forecast) response. Normally API credits are charged for this endpoint, but is free within one day after created a new forecast (through the Venue Search- or directly through the [New Foot Traffic Forecast](#input-attributes-new-forecast) endpoint).

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Week forecast endpoint: https://besttime.app/api/v1/forecasts/week
</aside>

<aside class="notice">
HTTP method: GET
</aside>


### Response attributes

The response attributes are exactly the same as the attributes in the 'new forecast' endpoint.  
 &nbsp;
See [new forecast reponse attributes](#response-attributes-new-forecast)

### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/week`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.

<!-- Content from _queryendpointsweekoverview.md -->

# Query weekoverview

> Query the week overview:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/weekoverview"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/weekoverview?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843'
```

```javascript
const params = new URLSearchParams({ 
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
});

fetch(`https://besttime.app/api/v1/forecasts/weekoverview?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```


### Input attributes

The 'query week' endpoint is used to retrieve all data from an existing forecast (every day of the week). The response structure is exactly the same as the [new forecast](#new-forecast) response. 

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Week overview endpoint: https://besttime.app/api/v1/forecasts/weekoverview
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns a JSON response like this:

```json
{
    "analysis": {
        "week_overview": [
            {
                "day_int": 0,
                "day_max": 100,
                "day_mean": 57,
                "day_rank_max": 1,
                "day_rank_mean": 6,
                "day_text": "Monday",
                "venue_closed": 4,
                "venue_open": 4
            },
            {
                "day_int": 1,
                "day_max": 96,
                "day_mean": 58,
                "day_rank_max": 3,
                "day_rank_mean": 5,
                "day_text": "Tuesday",
                "venue_closed": 4,
                "venue_open": 4
            },
            {
                "day_int": 2,
                "day_max": 99,
                "day_mean": 62,
                "day_rank_max": 2,
                "day_rank_mean": 1,
                "day_text": "Wednesday",
                "venue_closed": 4,
                "venue_open": 4
            },
            {
                "day_int": 3,
                "day_max": 87,
                "day_mean": 59,
                "day_rank_max": 6,
                "day_rank_mean": 4,
                "day_text": "Thursday",
                "venue_closed": 4,
                "venue_open": 4
            },
            {
                "day_int": 4,
                "day_max": 88,
                "day_mean": 61,
                "day_rank_max": 5,
                "day_rank_mean": 2,
                "day_text": "Friday",
                "venue_closed": 4,
                "venue_open": 4
            },
            {
                "day_int": 5,
                "day_max": 85,
                "day_mean": 60,
                "day_rank_max": 7,
                "day_rank_mean": 3,
                "day_text": "Saturday",
                "venue_closed": 4,
                "venue_open": 4
            },
            {
                "day_int": 6,
                "day_max": 93,
                "day_mean": 54,
                "day_rank_max": 4,
                "day_rank_mean": 7,
                "day_text": "Sunday",
                "venue_closed": 4,
                "venue_open": 4
            }
        ]
    },
    "forecast_updated_on": "2020-04-03T01:03:58.692417+00:00",
    "status": "OK"
}
```

### Response attributes Weekoverview


- **analysis** `object`  
 Containing the analysis.
 - analysis.**week_overview** `list`  
   List with day objects, containing overview details per day.  
  &nbsp;
       - analysis.weekoverview[day].**day_int** `int`  
       Day integer range `0` (Monday) to `6` (Sunday)  
       &nbsp;
       - analysis.weekoverview[day].**day_max** `int`  
       Indicating the maximum busyness percentage. Values (0 - 100%) are based on the hour with the most visitors of the day, relative to the biggest peak of the week for this venue.
       &nbsp;
       - analysis.weekoverview[day].**day_mean** `int`  
       Indicating the average busyness percentage (0 - 100%). Values are based on the total visitors (volume) of the day, relative to the biggest peak of the week for this venue. 
       &nbsp;
     - analysis.weekoverview[day].**day_rank_max** `int`  
       Day ranking based on the maximum busyness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most busy day of the week.  
       &nbsp;
     - analysis.weekoverview[day].**day_rank_mean** `int`  
       Day ranking based on mean busyness (total volume) of the day. Range `1` to `7`. E.g. `7` indicates the least busy day of the week.  
       &nbsp;
     - analysis.weekoverview[day].**day_text** `string`  
       Day name. E.g. `monday`  
       &nbsp;
     - analysis.weekoverview[day].**venue_closed** `int`/`string`  
       Hour of day when the venue closes. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.  
       &nbsp;
     - analysis.weekoverview[day].**venue_open** `int`/`string`  
       Hour of day when the venue opens. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day.  
       &nbsp;
- **forecast_updated_on** `TimeZone Aware DateTime string`  
 Date and time (Time Zone aware) of the original forecast.  
 &nbsp; 
- **status** `string`  
 Status of the response. Either `OK` or `Error`.  
 &nbsp; 

 ### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/weekoverview`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.

<!-- Content from _queryendpointsweekraw.md -->

# Query week raw

> Query the raw week data:

```python
import requests
 
url = "https://besttime.app/api/v1/forecasts/week/raw"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843',
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/week/raw?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843'
```

```javascript
const params = new URLSearchParams({ 
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
});

fetch(`https://besttime.app/api/v1/forecasts/week/raw?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes

The 'query week raw' endpoint is used to retrieve the raw data from an existing forecast (every day of the week).

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Week raw endpoint: https://besttime.app/api/v1/forecasts/week/raw
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns JSON structured like this:

```json
{
    "analysis": {
        "week_raw": [
            0.0,
            10.0,
            30.0,
            60.0,
            80.0,
            90.0,
            100.0,
            Other hours hidden 
            50.0,
            40.0,
            40.0,
            30.0,
            10.0,
            0.0,
            0.0
        ]
    },
    "epoch_analysis": 1585875838,
    "forecast_updated_on": "2020-04-03T01:03:58.692417+00:00",
    "venue_name": "McDonald's"
}
```

### Alternative split per day data
Using the endpoint `https://besttime.app/api/v1/forecasts/week/raw2` will result in the same response but split per day using the day window from 6am till 5am next day.

```json
{
    "analysis": {
        "week_raw": [
            {
                "day_int": 0,
                "day_raw": [
                    20,
                    30,
                    40,
                    50,
                    60,
                    ...
                    60,
                    50,
                    40,
                    30,
                    20,
                    0,
                    20,
                    20
                ]
            },
            ....
        ]
    },
    "status": "OK",
    "window": {
        "day_window_end_int": 6,
        "day_window_end_txt": "Monday",
        "day_window_start_int": 0,
        "day_window_start_txt": "Monday",
        "time_window_end": 5,
        "time_window_end_12h": "5AM",
        "time_window_start": 6,
        "time_window_start_12h": "6AM",
        "week_window": "Monday 6AM until Monday 5AM next week"
    }
}
```


### Combine a new forecast with this query in a single API call
This query endpoint takes data from an earlier forecasted venue. You can also combine a fresh forecast and get the results from this query endpoint using:

-  HTTP method: `POST` (instead of `GET`)
-  The same API query endpoint URL `https://besttime.app/api/v1/forecasts/week/raw`
-  `venue_name` and `venue_address` as input or `venue_id`
- The input attributes from this query endpoint

See the [New Forecast](#forecast-new-link) endpoint for more information on the `venue_name` and `venue_address` input. This will be counted as new forecast credits instead of a query credit.



<!-- Content from _venuecollections.md -->

# Venue collections

Collections can be used to group venues together. Each collection has an unique 36 `collection_id` and an optional name.
Venues inside a collection are managed using the `venue_id` of each venue. 
Your existing collections can be also viewed on the [Collection page](https://besttime.app/api/v1/collection_list). On the page, click on a collection_id to see which venues are inside or to open the collection in the Radar tool.

Through the collections API endpoints, you can create or delete collections, and add or remove venues to/from an existing collection. 

There are multiple ways to use a collection in combination with the other BestTime tools/ API endpoints 
- Manually add venues to a collection to group them and later call the collection to simply know which `venue_id`’s belong together.
- Pass a collection_id to a [New forecast](#new-foot-traffic-forecast) to automatically add one or multiple successful venues to an existing collection. 
- The Radar tool and Venue Filter accepts a collection_id as input show and filter only on the venues inside that collection
- The Venue Search tool and API endpoint automatically creates a new collection with a new search query, with the search query as collection name. The Venue Search API endpoint also accepts an existing collection id. This will merge the new search results with the given collection.

## Create a collection

```python
import requests
 
url = "https://besttime.app/api/v1/collection"

params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
    'collection_id': 'col_51387131543761435650505241346a39',
    'name': 'Supermarkets in Los Angeles, CA'
}

response = requests.request("POST", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request POST 'https://besttime.app/api/v1/collection?api_key_private=pri_s43661721b084d36b8f469a2c012e754&
collection_id=col_51387131543761435650505241346a39&
name=Supermarkets%20in%20Los%20Angeles%20CA'
```

```javascript
const params = new URLSearchParams({ 
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
    'collection_id': 'col_51387131543761435650505241346a39',
    'name': 'Supermarkets in Los Angeles, CA'
});

fetch(`https://besttime.app/api/v1/collection?${params}`, {
  method: 'POST'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes

- **collection_id** `string` <span style="color:blue">OPTIONAL</span>  
 The unique ID for the collection, 36 characters long. A new unique `collection_id` will be generated if no self generated id is included in the request.
 &nbsp; 
- **name** `string` <span style="color:blue">OPTIONAL</span>  
 Name for the collection. Does not have to be unique. Maximum `128` characters long.
 &nbsp; 
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Collection create endpoint: https://besttime.app/api/v1/collection
</aside>

<aside class="notice">
HTTP method: POST
</aside>


> The above request returns JSON structured like this:

```json
{
    "collection": {
        "api_key_private": "pri_s43661721b084d36b8f469a2c012e754",
        "collection_id": "col_51387131543761435650505241346a39",
        "name": "Supermarkets in Los Angeles, CA"
    },
    "status": "OK"
}
```


## Add venues to a collection

```python
import requests
 
url = "https://besttime.app/api/v1/collection/col_51387131543761435650505241346a39/ven_51387131543761435650505241346a394a6432395362654a496843"

params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
}

response = requests.request("POST", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request POST 'https://besttime.app/api/v1/collection/col_51387131543761435650505241346a39/ven_51387131543761435650505241346a394a6432395362654a496843?api_key_private=pri_s43661721b084d36b8f469a2c012e754
```

```javascript
const params = new URLSearchParams({ 
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
});

fetch(`https://besttime.app/api/v1/collection/col_51387131543761435650505241346a39/ven_51387131543761435650505241346a394a6432395362654a496843?${params}`, {
  method: 'POST'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes

- **collection_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the collection, 36 characters long.
 &nbsp; 
- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 ID of the venue to be added to the collection.
 &nbsp; 
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Collection Add Venue endpoint: https://besttime.app/api/v1/collection/{{collection_id}}/{{venue_id}}
</aside>

<aside class="notice">
HTTP method: POST
</aside>


> The above request returns JSON structured like this:

```json
{
    "collection_id": "col_51387131543761435650505241346a39",
    "message": "Venue added to collection",
    "status": "OK",
    "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843"
}
```

## Collection Venues

Returns a list with all venue_id's of venues in the collection

```python
import requests
 
url = "https://besttime.app/api/v1/collection/col_51387131543761435650505241346a39

params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
}

response = requests.request("GET", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/collection/col_51387131543761435650505241346a39?api_key_private=pri_s43661721b084d36b8f469a2c012e754
```

```javascript
const params = new URLSearchParams({ 
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
});

fetch(`https://besttime.app/api/v1/collection/col_51387131543761435650505241346a39?${params}`, {
  method: 'GET'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes

- **collection_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the collection, 36 characters long.
 &nbsp; 
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Collection Venues endpoint: https://besttime.app/api/v1/collection/{{collection_id}}
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns JSON structured like this:

```json
{
    "collection_id": "col_51387131543761435650505241346a39",
    "status": "OK",
    "venue_ids": [
        "ven_51387131543761435650505241346a394a6432395362654a496843"
    ]
}
```

## Collection Remove venue

Removes a venue from the collection using the `venue_id`.

```python
import requests
 
url = "https://besttime.app/api/v1/collection/col_51387131543761435650505241346a39/ven_51387131543761435650505241346a394a6432395362654a496843"

params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
}

response = requests.request("DELETE", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request DELETE 'https://besttime.app/api/v1/collection/col_51387131543761435650505241346a39/ven_51387131543761435650505241346a394a6432395362654a496843?api_key_private=pri_s43661721b084d36b8f469a2c012e754
```

```javascript
const params = new URLSearchParams({ 
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
});

fetch(`https://besttime.app/api/v1/collection/col_51387131543761435650505241346a39/ven_51387131543761435650505241346a394a6432395362654a496843?${params}`, {
  method: 'DELETE'
}).then(function(data) { 
  console.log(data); 
});
```

### Input attributes

- **collection_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the collection, 36 characters long.
 &nbsp; 
- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 ID of the venue to be removed from the collection.
 &nbsp; 
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Collection Remove Venue endpoint: https://besttime.app/api/v1/collection/{{collection_id}}/{{venue_id}}
</aside>

<aside class="notice">
HTTP method: DELETE
</aside>


> The above request returns JSON structured like this:

```json
{
    "collection_id": "col_51387131543761435650505241346a39",
    "message": "Venue deleted from collection",
    "status": "OK",
    "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843"
}
```


## Collection delete

Delete a collection using the `collection_id`. Deleting a collection does not affect the venues listed in the collection itself.


```python
import requests
 
url = "https://besttime.app/api/v1/collection"

params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
    'collection_id': 'col_51387131543761435650505241346a39',
}

response = requests.request("DELETE", url, params=params)
print(response.json())
```

```shell
# cURL
curl --location --request DELETE 'https://besttime.app/api/v1/collection?api_key_private=pri_s43661721b084d36b8f469a2c012e754&
collection_id=col_51387131543761435650505241346a39'
```

```javascript
const params = new URLSearchParams({ 
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
    'collection_id': 'col_51387131543761435650505241346a39'
});

fetch(`https://besttime.app/api/v1/collection?${params}`, {
  method: 'DELETE'
}).then(function(data) { 
  console.log(data); 
});

```

### Input attributes

- **collection_id** `string` <span style="color:blue">OPTIONAL</span>  
 The unique ID for the collection, 36 characters long. 
 &nbsp; 
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-reference)  
 &nbsp; 

<aside class="notice">
Collection Delete endpoint: https://besttime.app/api/v1/collection/{{collection_id}}
</aside>

<aside class="notice">
HTTP method: DELETE
</aside>

> The above request returns JSON structured like this:

```json
{
    "message": "collection_id col_51387131543761435650505241346a39 deleted",
    "status": "OK"
}
```

