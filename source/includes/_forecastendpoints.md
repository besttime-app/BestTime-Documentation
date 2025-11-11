
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
    "status": "OK",
    "venue_info": {
        "venue_id": "ven_454e4e686e4a7046453659526b6f775a6c3673525158614a496843",
        "venue_name": "Empire State Building",
        "venue_address": "20 W 34th St. New York, NY 10001 United States",
        "venue_address_list": [
            "20 W 34th St.",
            "New York, NY 10001",
            "United States"
        ],
        "venue_timezone": "America/New_York",
        "venue_dwell_time_min": 45,
        "venue_dwell_time_max": 120,
        "venue_dwell_time_avg": 82,
        "venue_type": "HISTORICAL",
        "venue_types": [
            "historical_landmark",
            "historical_place_museum",
            "observation_deck",
            "tourist_attraction"
        ],
        "venue_lat": 40.7484405,
        "venue_lon": -73.98566439999999,
        "rating": 4.7,
        "reviews": 121628,
        "price_level": 0
    },
    "analysis": [
        {
            "day_info": {
                "day_int": 0,
                "day_text": "Monday",
                "venue_open": 11,
                "venue_closed": 21,
                "day_rank_mean": 6,
                "day_rank_max": 6,
                "day_mean": 79,
                "day_max": 82,
                "venue_open_close_v2": {
                    "24h": [
                        {
                            "opens": 11,
                            "closes": 21,
                            "opens_minutes": 0,
                            "closes_minutes": 0
                        }
                    ],
                    "12h": [
                        "11am–9pm"
                    ],
                    "special_day": null,
                    "open_24h": false,
                    "crosses_midnight": false,
                    "day_text": "Monday"
                },
                "note": "Update: venue_open_close_v2 replaces venue_open and venue_closed and supports multiple opening times per day."
            },
            "busy_hours": [],
            "quiet_hours": [
                20,
                21
            ],
            "peak_hours": [],
            "surge_hours": {
                "most_people_come": 9,
                "most_people_leave": 22
            },
            "hour_analysis": [
                {
                    "hour": 6,
                    "intensity_nr": -1,
                    "intensity_txt": "Below average"
                },
                ... Other hours hidden. See full JSON example link below
            ],
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
            ]
        },
        ... Other days hidden. See full JSON example link below
    ],
    "epoch_analysis": "1583314752"
}
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
     - analysis[day_int].day_info.**day_mean** `int`
       Indicating the average busyness percentage (0 - 100%). Values are based on the total visitors (volume) of the day, relative to the biggest peak of the week for this venue.
       &nbsp;
     - analysis[day_int].day_info.**day_max** `int`
       Indicating the maximum busyness percentage. Values (0 - 100%) are based on the hour with the most visitors of the day, relative to the biggest peak of the week for this venue.
       &nbsp;
     - analysis[day_int].day_info.**venue_closed** `int`/`string` <span style="color:red">DEPRECATED</span>
       Hour of day when the venue closes. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day. Deprecated, use `venue_open_close_v2` instead.
       &nbsp;
     - analysis[day_int].day_info.**venue_open** `int`/`string` <span style="color:red">DEPRECATED</span>
       Hour of day when the venue opens. Range `0` to `23` hour. States `'closed'` when the venue is closed whole day. Deprecated, use `venue_open_close_v2` instead.
       &nbsp;
     - analysis[day_int].day_info.**venue_open_close_v2** `object`
       Object with open and close times for the venue. The object contains `day_text`, `open_24h`, `crosses_midnight`, two lists: `24h` and `12h`, and optional `special_day`. The `24h` list contains open and close times for the venue in 24 hour notation. The `12h` list contains open and close times for the venue in 12 hour notation. A venue can have multiple opening times per day. Note: requires refreshing the foot traffic forecast if the foot traffic forecast is outdated.
        &nbsp;
        - analysis[day_int].day_info.venue_open_close_v2.**day_text** `string`
          Day name for this day. E.g. `"Monday"`.
          &nbsp;
        - analysis[day_int].day_info.venue_open_close_v2.**open_24h** `bool`
          Indicates if the venue is open 24 hours on this day.
          &nbsp;
        - analysis[day_int].day_info.venue_open_close_v2.**crosses_midnight** `bool`
          Indicates if any opening period crosses midnight.
          &nbsp;
        - analysis[day_int].day_info.venue_open_close_v2.**24h** `list`
          List with objects describing each opening period in 24 hour notation. Every object contains `opens`, `opens_minutes`, `closes`, and `closes_minutes`.
          &nbsp;
        - analysis[day_int].day_info.venue_open_close_v2.**12h** `list`
          List with open and close times for the venue in 12 hour notation.
          &nbsp;
        - analysis[day_int].day_info.venue_open_close_v2.**special_day** `object|null`
          Optional object describing holiday/special-day overrides. Either `null` or an object with `message` and `name` fields.
          &nbsp;
     - analysis[day_int].day_info.**note** `string`
       Optional note about the day_info structure or updates.
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
 - venue_info.**venue_address_list** `list`
   Address of the venue broken down into a list of components. Typically contains street address, city/state/zip, and country as separate elements.
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
- venue_info.**venue_open_close_v2** `object`
  Returned in both success and error payloads when opening hours are available, so you can inspect the latest schedule even if not enough foot-traffic data exists for a forecast. Structure matches `analysis.day_info.venue_open_close_v2`, including the optional `special_day` that is either `null` or `{ "message": "...", "name": "..." }`.
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
