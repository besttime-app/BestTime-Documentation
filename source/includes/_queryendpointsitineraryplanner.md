# Query itinerary planner

> Generate an ordered nightlife or sightseeing itinerary from forecasted venues.

This endpoint powers the BestTime planner UI on the website. It builds a route from either a search area, a [collection](#venue-collections), or an explicit list of `venue_id`s and returns ordered stops, visit timings, map coordinates, and planner reasoning.

<aside class="warning">
The itinerary planner is currently in beta. Planner behavior and the exact response shape may evolve based on user feedback.
</aside>

## Nightlife route from a city

```python
import requests

url = "https://besttime.app/api/v1/itineraries/plan"

payload = {
    "api_key_private": "pri_50990bf1f8828f6abbf6152013113c6b",
    "preset": "nightlife",
    "day_int": 4,
    "day_part": "night",
    "city_id": 77528,
    "stop_count": 4,
    "transfer_buffer_min": 10,
    "distance_penalty": 0.2,
    "types": ["BAR", "BEER", "BREWERY", "CLUBS", "WINERY"]
}

response = requests.post(url, json=payload)
print(response.json())
```

```shell
# cURL
curl --location --request POST 'https://besttime.app/api/v1/itineraries/plan' \
--header 'Content-Type: application/json' \
--data-raw '{
  "api_key_private": "pri_50990bf1f8828f6abbf6152013113c6b",
  "preset": "nightlife",
  "day_int": 4,
  "day_part": "night",
  "city_id": 77528,
  "stop_count": 4,
  "transfer_buffer_min": 10,
  "distance_penalty": 0.2,
  "types": ["BAR", "BEER", "BREWERY", "CLUBS", "WINERY"]
}'
```

```javascript
fetch('https://besttime.app/api/v1/itineraries/plan', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    api_key_private: 'pri_50990bf1f8828f6abbf6152013113c6b',
    preset: 'nightlife',
    day_int: 4,
    day_part: 'night',
    city_id: 77528,
    stop_count: 4,
    transfer_buffer_min: 10,
    distance_penalty: 0.2,
    types: ['BAR', 'BEER', 'BREWERY', 'CLUBS', 'WINERY']
  })
}).then(function(response) {
  return response.json();
}).then(function(data) {
  console.log(data);
});
```

### Input attributes itinerary planner

The itinerary planner selects and sequences venues using forecasted foot traffic, venue dwell time, venue quality filters, and a simple distance heuristic. It returns a route that can be shown on a map or used for guided playback experiences.

- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-reference)
 &nbsp;
- **preset** `string` <span style="color:orange">REQUIRED</span>  
 Planner mode. Possible values are `nightlife` or `sightseeing`.
 &nbsp;
- **strategy** `string` <span style="color:blue">OPTIONAL</span>  
 Route scoring strategy. Possible values are `rising_energy`, `pre_peak`, or `offpeak`. If omitted, the endpoint automatically selects `rising_energy` for `nightlife` and `offpeak` for `sightseeing`.
 &nbsp;

- **city_id** `int` <span style="color:blue">OPTIONAL</span>  
 Search using a stored city center and radius from the BestTime city table. This is one of the three possible candidate source modes and cannot be combined with `lat`, `lng`, or `radius`.
 &nbsp;
- **lat** `float` <span style="color:blue">OPTIONAL</span>  
 Search latitude for coordinate mode. Must be combined with `lng` and `radius`.
 &nbsp;
- **lng** `float` <span style="color:blue">OPTIONAL</span>  
 Search longitude for coordinate mode. Must be combined with `lat` and `radius`.
 &nbsp;
- **radius** `int` <span style="color:blue">OPTIONAL</span>  
 Search radius in meters for coordinate mode. Min `1`, max `200000`. Must be combined with `lat` and `lng`.
 &nbsp;
- **collection_id** `string` <span style="color:blue">OPTIONAL</span>  
 Plan only from venues inside an existing collection. See more info on [Collections](#venue-collections).
 &nbsp;
- **venue_ids** `list` <span style="color:blue">OPTIONAL</span>  
 Plan only from a list of specific `venue_id`s.
 &nbsp;

- **day_int** `int` <span style="color:orange">REQUIRED</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday). See [Forecast day window and weekdays](#forecast-day-window-and-weekdays).
 &nbsp;
- **day_part** `string` <span style="color:blue">OPTIONAL</span>  
 Named time window. Possible values are `morning`, `afternoon`, `evening`, or `night`. These map to the following hour windows inside the BestTime logical day: `morning=06-12`, `afternoon=12-18`, `evening=18-23`, `night=21-03`.
 &nbsp;
- **hour_min** `int` <span style="color:blue">OPTIONAL</span>  
 Custom start hour, using 24 hour notation. Range `0` to `23`.
 &nbsp;
- **hour_max** `int` <span style="color:blue">OPTIONAL</span>  
 Custom end hour, using 24 hour notation. Range `0` to `23`.
 &nbsp;

- **stop_count** `int` <span style="color:blue">OPTIONAL</span>  
 Maximum number of stops to generate. Default `4`, min `1`, max `20`.
 &nbsp;
- **transfer_buffer_min** `int` <span style="color:blue">OPTIONAL</span>  
 Extra minutes added between stops. Default `10`, min `0`, max `180`.
 &nbsp;
- **distance_penalty** `float` <span style="color:blue">OPTIONAL</span>  
 Distance heuristic strength between `0` and `1`. Default `0.0`. This is a route-ordering bias based on straight-line distance, not actual walking or driving time.
 &nbsp;
- **iconic_bias** `bool` <span style="color:blue">OPTIONAL</span>  
 Bias sightseeing routes toward iconic venues with stronger rating/review signals. If omitted, this defaults to `true` for `sightseeing` and `false` for `nightlife`.
 &nbsp;

- **types** `list` <span style="color:blue">OPTIONAL</span>  
 Filter the candidate venues to one or more venue types.
 &nbsp;
- **rating_min** `float` <span style="color:blue">OPTIONAL</span>  
 Minimum venue rating. Range `0` to `5`.
 &nbsp;
- **rating_max** `float` <span style="color:blue">OPTIONAL</span>  
 Maximum venue rating. Range `0` to `5`.
 &nbsp;
- **reviews_min** `int` <span style="color:blue">OPTIONAL</span>  
 Minimum number of venue reviews. Min `0`.
 &nbsp;
- **reviews_max** `int` <span style="color:blue">OPTIONAL</span>  
 Maximum number of venue reviews. Min `0`.
 &nbsp;
- **price_min** `int` <span style="color:blue">OPTIONAL</span>  
 Minimum price level. Range `1` to `5`.
 &nbsp;
- **price_max** `int` <span style="color:blue">OPTIONAL</span>  
 Maximum price level. Range `1` to `5`.
 &nbsp;
- **venue_whitelist_ids** `list` <span style="color:blue">OPTIONAL</span>  
 Restrict the planner to these `venue_id`s only.
 &nbsp;
- **venue_blacklist_ids** `list` <span style="color:blue">OPTIONAL</span>  
 Exclude these `venue_id`s from the generated plan.
 &nbsp;

<aside class="notice">
Exactly one candidate source must be provided: a search area (`city_id` or `lat` + `lng` + `radius`), a `collection_id`, or a list of `venue_ids`.
</aside>

<aside class="notice">
`city_id` cannot be combined with `lat`, `lng`, or `radius`.
</aside>

<aside class="notice">
Either `day_part` or both `hour_min` and `hour_max` must be provided. `day_part` cannot be combined with `hour_min` and `hour_max`.
</aside>

<aside class="notice">
Itinerary planner endpoint: https://besttime.app/api/v1/itineraries/plan
</aside>

<aside class="notice">
HTTP method: POST
</aside>

<aside class="notice">
JSON request body required
</aside>

> The above request returns a JSON response like this:

```json
{
  "status": "OK",
  "preset": "nightlife",
  "strategy": "rising_energy",
  "source_mode": "search_area",
  "window": {
    "day_int": 4,
    "hour_min": 21,
    "hour_max": 3,
    "label": "Friday night"
  },
  "distance_penalty": 0.2,
  "stops_n": 2,
  "stops": [
    {
      "order": 1,
      "venue_id": "ven_4b6dbf8f8fbc5a0001",
      "venue_name": "Door 74",
      "venue_address": "Reguliersdwarsstraat 74, Amsterdam, Netherlands",
      "venue_type": "BAR",
      "venue_rating": 4.7,
      "venue_reviews": 1800,
      "venue_price_level": 3,
      "venue_lat": 52.3650,
      "venue_lng": 4.8913,
      "arrival_time": {
        "hour": 21,
        "minute": 0,
        "label_24h": "21:00",
        "label_12h": "9pm"
      },
      "departure_time": {
        "hour": 22,
        "minute": 5,
        "label_24h": "22:05",
        "label_12h": "10:05pm"
      },
      "planned_duration_min": 65,
      "transfer_buffer_min": 10,
      "dwell_time_hint_min": 50,
      "dwell_time_hint_max": 80,
      "iconic_score": 40.51,
      "forecast_summary": {
        "avg_busy": 82.5,
        "arrival_busy": 78,
        "departure_busy": 90,
        "peak_busy": 100,
        "peak_hour": 23
      },
      "selected_day_foot_traffic": [0, 0, 0, 0, 0, 5, 12, 22, 34, 48, 61, 70, 74, 78, 82, 88, 94, 100, 96, 84, 68, 42, 18, 8],
      "planned_window_slots": {
        "start": 15,
        "end": 16
      },
      "planned_window_minutes": {
        "start": 900,
        "end": 965
      },
      "reason_tags": ["rising_energy", "avoid_dead_time"],
      "distance_from_previous_m": 0,
      "opening_hours": {
        "open": 18,
        "close": 3
      }
    },
    {
      "order": 2,
      "venue_id": "ven_4b6dbf8f8fbc5a0002",
      "venue_name": "Law & Order Cocktail Bar",
      "venue_address": "Voetboogstraat 4, Amsterdam, Netherlands",
      "venue_type": "BAR",
      "venue_rating": 4.5,
      "venue_reviews": 920,
      "venue_price_level": 2,
      "venue_lat": 52.3690,
      "venue_lng": 4.8890,
      "arrival_time": {
        "hour": 22,
        "minute": 15,
        "label_24h": "22:15",
        "label_12h": "10:15pm"
      },
      "departure_time": {
        "hour": 23,
        "minute": 15,
        "label_24h": "23:15",
        "label_12h": "11:15pm"
      },
      "planned_duration_min": 60,
      "transfer_buffer_min": 10,
      "dwell_time_hint_min": 45,
      "dwell_time_hint_max": 70,
      "iconic_score": 34.33,
      "forecast_summary": {
        "avg_busy": 91.0,
        "arrival_busy": 88,
        "departure_busy": 94,
        "peak_busy": 100,
        "peak_hour": 23
      },
      "selected_day_foot_traffic": [0, 0, 0, 0, 0, 0, 8, 16, 26, 38, 50, 60, 70, 78, 84, 88, 92, 96, 100, 92, 76, 58, 34, 16],
      "planned_window_slots": {
        "start": 16,
        "end": 17
      },
      "planned_window_minutes": {
        "start": 975,
        "end": 1035
      },
      "reason_tags": ["rising_energy", "avoid_dead_time", "distance_penalty"],
      "distance_from_previous_m": 476,
      "opening_hours": {
        "open": 18,
        "close": 3
      }
    }
  ],
  "path": [
    [52.3650, 4.8913],
    [52.3690, 4.8890]
  ],
  "playback": {
    "supported": true,
    "steps": [
      {
        "order": 1,
        "venue_id": "ven_4b6dbf8f8fbc5a0001",
        "venue_name": "Door 74",
        "arrival_time": {
          "hour": 21,
          "minute": 0,
          "label_24h": "21:00",
          "label_12h": "9pm"
        },
        "departure_time": {
          "hour": 22,
          "minute": 5,
          "label_24h": "22:05",
          "label_12h": "10:05pm"
        }
      },
      {
        "order": 2,
        "venue_id": "ven_4b6dbf8f8fbc5a0002",
        "venue_name": "Law & Order Cocktail Bar",
        "arrival_time": {
          "hour": 22,
          "minute": 15,
          "label_24h": "22:15",
          "label_12h": "10:15pm"
        },
        "departure_time": {
          "hour": 23,
          "minute": 15,
          "label_24h": "23:15",
          "label_12h": "11:15pm"
        }
      }
    ]
  }
}
```

### Response fields

Top level response fields:

- **status** `string`  
 API status. Returns `OK` for successful requests.
 &nbsp;
- **preset** `string`  
 Echoes the planner preset used for the route.
 &nbsp;
- **strategy** `string`  
 The final scoring strategy applied by the planner.
 &nbsp;
- **source_mode** `string`  
 Indicates the candidate source that was used. Possible values are `search_area`, `collection_id`, or `venue_ids`.
 &nbsp;
- **window** `object`  
 Selected day and time window for the route, including the human readable `label`.
 &nbsp;
- **distance_penalty** `float`  
 The applied route-ordering distance heuristic strength.
 &nbsp;
- **stops** `list`  
 Ordered list of suggested route stops.
 &nbsp;
- **stops_n** `int`  
 Number of returned stops.
 &nbsp;
- **path** `list`  
 Ordered coordinate pairs for simple map rendering.
 &nbsp;
- **playback** `object`  
 Playback metadata for guided walkthrough or presentation experiences.
 &nbsp;

Each stop object includes core route and forecast data such as:

- **order** `int`
- **venue_id** `string`
- **venue_name** `string`
- **venue_address** `string`
- **venue_type** `string`
- **venue_lat** `float`
- **venue_lng** `float`
- **arrival_time** `object`
- **departure_time** `object`
- **planned_duration_min** `int`
- **transfer_buffer_min** `int`
- **forecast_summary** `object`
- **reason_tags** `list`
- **distance_from_previous_m** `int`
- **opening_hours** `object`
- **selected_day_foot_traffic** `list`
- **planned_window_slots** `object`
- **planned_window_minutes** `object`

Nested response objects are intentionally compact:
- `forecast_summary` describes the predicted crowd levels for the scheduled visit window
- `arrival_time` and `departure_time` include hour, minute, and both 24h / 12h labels
- `path` is a simple ordered coordinate path, not turn-by-turn navigation
- `playback.steps` supports guided map playback or presentation experiences

## Curated sightseeing route from a collection

```python
import requests

url = "https://besttime.app/api/v1/itineraries/plan"

payload = {
    "api_key_private": "pri_50990bf1f8828f6abbf6152013113c6b",
    "preset": "sightseeing",
    "day_int": 5,
    "day_part": "afternoon",
    "collection_id": "col_12345678901234567890123456789012",
    "stop_count": 3,
    "iconic_bias": True,
    "types": ["MUSEUM", "MONUMENT", "TOURIST_DESTINATION"]
}

response = requests.post(url, json=payload)
print(response.json())
```

```shell
# cURL
curl --location --request POST 'https://besttime.app/api/v1/itineraries/plan' \
--header 'Content-Type: application/json' \
--data-raw '{
  "api_key_private": "pri_50990bf1f8828f6abbf6152013113c6b",
  "preset": "sightseeing",
  "day_int": 5,
  "day_part": "afternoon",
  "collection_id": "col_12345678901234567890123456789012",
  "stop_count": 3,
  "iconic_bias": true,
  "types": ["MUSEUM", "MONUMENT", "TOURIST_DESTINATION"]
}'
```

```javascript
fetch('https://besttime.app/api/v1/itineraries/plan', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    api_key_private: 'pri_50990bf1f8828f6abbf6152013113c6b',
    preset: 'sightseeing',
    day_int: 5,
    day_part: 'afternoon',
    collection_id: 'col_12345678901234567890123456789012',
    stop_count: 3,
    iconic_bias: true,
    types: ['MUSEUM', 'MONUMENT', 'TOURIST_DESTINATION']
  })
}).then(function(response) {
  return response.json();
}).then(function(data) {
  console.log(data);
});
```

> A collection-based sightseeing response will use the same top-level structure, but typically returns `source_mode: "collection_id"` and applies the quieter sightseeing strategy defaults.

```json
{
  "status": "OK",
  "preset": "sightseeing",
  "strategy": "offpeak",
  "source_mode": "collection_id",
  "window": {
    "day_int": 5,
    "hour_min": 12,
    "hour_max": 18,
    "label": "Saturday afternoon"
  },
  "distance_penalty": 0.0,
  "stops_n": 2,
  "stops": [
    {
      "order": 1,
      "venue_id": "ven_6a4f8a5c0000000000000001",
      "venue_name": "Anchor Museum",
      "arrival_time": {
        "label_24h": "12:00"
      },
      "departure_time": {
        "label_24h": "13:30"
      },
      "forecast_summary": {
        "avg_busy": 18.0,
        "peak_busy": 42,
        "peak_hour": 15
      },
      "reason_tags": ["full_stay_quiet_window", "iconic_bias"]
    },
    {
      "order": 2,
      "venue_id": "ven_6a4f8a5c0000000000000002",
      "venue_name": "City Monument",
      "arrival_time": {
        "label_24h": "13:40"
      },
      "departure_time": {
        "label_24h": "14:40"
      },
      "forecast_summary": {
        "avg_busy": 22.5,
        "peak_busy": 48,
        "peak_hour": 16
      },
      "reason_tags": ["full_stay_quiet_window", "iconic_bias"]
    }
  ],
  "path": [
    [40.7128, -74.0060],
    [40.7133, -74.0048]
  ],
  "playback": {
    "supported": true,
    "steps": [
      {
        "order": 1,
        "venue_id": "ven_6a4f8a5c0000000000000001",
        "venue_name": "Anchor Museum"
      },
      {
        "order": 2,
        "venue_id": "ven_6a4f8a5c0000000000000002",
        "venue_name": "City Monument"
      }
    ]
  }
}
```
