# Query endpoints

All query endpoints are used to retrieve all data or specific analysis from an existing forecast.
The `venue_id` is the primary parameter to query an excisting forecast.

## Query week

> Query the week (whole forecast):

```python
import requests
import json

url = "https://BestTime.app/api/v1/query/week/"

headers = {
    'Content-Type': 'application/json'
}

payload = json.dumps({
    "api_key_public": "352a9addc0ac4c599572e56f504080d3",
	"venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw=="
})

response = requests.request("POST", url, headers=headers, data = payload)

response_dict = json.loads(response.text.encode('utf8'))
```

```shell
# cURL
curl --location --request POST 'https://BestTime.app/api/v1/query/week/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key_public": "352a9addc0ac4c599572e56f504080d3",
	"venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw=="
}	'
```

```javascript
var settings = {
  "url": "https://BestTime.app/api/v1/query/week/",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    	"api_key_public": "352a9addc0ac4c599572e56f504080d3",
	    "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw=="
    }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> The above request returns a JSON structured similar as the [new forecast](#new-forecast) endpoint

> Click <a href="https://github.com/besttime-app/slate/blob/master/source/examples/forecast_new/forecast_new_response.json" target="_blank">here</a> for the full JSON response

### Input attributes

The 'query week' endpoint is used to retrieve all data from an existing forecast (every day of the week). The response structure is exactly the same as the [new forecast](#new-forecast) response. 

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'forecast list' endpoint which shows all previously forecasted venues.
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-keys)
 &nbsp; 

<aside class="notice">
New forecast endpoint: https://BestTime.app/api/v1/query/week/
</aside>

<aside class="notice">
HTTP method: POST
</aside>


### Response attributes

The response attributes are exactly the same as the attributes in the 'new forecast' endpoint.  
 &nbsp;
See [new forecast reponse attributes](#responseattributesnewforecast)


## Query day 

> Query one day of the week:

```python
import requests
import json

url = "https://BestTime.app/api/v1/query/day/"

headers = {
    'Content-Type': 'application/json'
}

payload = json.dumps({
    "api_key_public": "352a9addc0ac4c599572e56f504080d3",
	"venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
    "day_int": 3
})

response = requests.request("POST", url, headers=headers, data = payload)

response_dict = json.loads(response.text.encode('utf8'))
```

```shell
# cURL
curl --location --request POST 'https://BestTime.app/api/v1/query/day/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key_public": "352a9addc0ac4c599572e56f504080d3",
	"venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
    "day_int": 3
}	'
```

```javascript
var settings = {
  "url": "https://BestTime.app/api/v1/query/day/",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    	"api_key_public": "352a9addc0ac4c599572e56f504080d3",
	    "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
        "day_int": 3
    }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

> The above request returns a JSON reponse like this:

```json
  {
    "busy_hours": [
        "9",
        "10",
        "11",
        "12",
        "13",
        "16",
        "17",
        "18"
    ],
    "day_info": {
        "day_int": 0,
        "day_rank_max": 6,
        "day_rank_mean": 4,
        "day_text": "Monday",
        "venue_closed": 4,
        "venue_open": 4
    },
    "day_int": 0,
    "epoch_analysis": 1583400856,
    "hour_analysis": [
        {
            "hour": 6,
            "intensity_nr": -1,
            "intensity_txt": "Below average"
        },
        {
            "hour": 7,
            "intensity_nr": -1,
            "intensity_txt": "Below average"
        },
        ... other hours hidden. See below for the full JSON response examoke ...
    ],
    "peak_hours": [
        {
            "peak_delta_mean_week": 29,
            "peak_end": 23,
            "peak_intensity": 4,
            "peak_max": 11,
            "peak_start": 8
        }
    ],
    "quiet_hours": [
        "6",
        "1",
        "2",
        "3",
        "4",
        "5"
    ],
    "surge_hours": {
        "most_people_come": 8,
        "most_people_leave": 0
    },
    "updated_on": "2020-03-05T09:34:16.836061+00:00",
    "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
    "venue_name": "McDonald's"
}
```

> Click <a href="https://github.com/besttime-app/slate/blob/master/source/examples/query_day/query_day_response.json" target="_blank">here</a> for the full JSON response

### Input attributes Query Day

The 'query day' endpoint is used to retrieve all analysis from an existing forecast for a specific day of the week.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'forecast list' endpoint which shows all previously forecasted venues.
 &nbsp; 
- **day_int** `int` <span style="color:orange">REQUIRED</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday).
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-keys)
 &nbsp; 

<aside class="notice">
New forecast endpoint: https://BestTime.app/api/v1/query/day/
</aside>

<aside class="notice">
HTTP method: POST
</aside>


### Response attributes




## Query hour 

## Query current hour

## Query peak hours

## Query busy hours

## Query quiet hours

## Query surge hours





