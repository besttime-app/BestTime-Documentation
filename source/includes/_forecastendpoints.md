
# Forecasts endpoints


## New forecast

> Create a new forecast:

```python
import requests
import json

url = "https://BestTime.app/api/v1/forecast/new/"

headers = {
    'Content-Type': 'application/json'
}

payload = json.dumps({
    "venue_name" : "McDonald's",
	"venue_address" : "1201 Ocean Ave, San Francisco, CA 94112, United States",
    'api_key_private': 'e267713ecda84c77a055294dbb12c6d4'
})

response = requests.request("POST", url, headers=headers, data = payload)

response_dict = json.loads(response.text.encode('utf8'))
```

```shell
# cURL
curl --location --request POST 'https://BestTime.app/api/v1/forecast/new/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "venue_name" : "McDonald'\''s",
	"venue_address" : "1201 Ocean Ave, San Francisco, CA 94112, United States",
	"api_key_private": "e267713ecda84c77a055294dbb12c6d4"
}	'
```

```javascript
var settings = {
  "url": "https://BestTime.app/api/v1/forecast/new/",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    "venue_name" : "McDonald's",
	"venue_address" : "1201 Ocean Ave, San Francisco, CA 94112, United States",
    "api_key_private":"e267713ecda84c77a055294dbb12c6d4"
    }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
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
                "venue_closed": 6,
                "venue_open": 23
            },
            "hour_analysis": [
                {
                    "hour": 6,
                    "intensity_nr": -1,
                    "intensity_txt": "Below average"
                },
                ... Other hours. See full example link below
            ],
            "peak_hours": [
                {
                    "peak_start": 8,
                    "peak_max": 11,
                    "peak_end": 23,
                    "peak_delta_mean_week": 29,
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
            "change_hours": {
                "most_people_come": 8,
                "most_people_leave": 22
            },
        },
        ... Other days hidden. See full example link below
    ],
    "epoch_analysis": "1583314752",
    "status": "OK",
    "venue_info": {
        "venue_address": "1201 Ocean Ave San Francisco, CA 94112 United States",
        "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles"
    }
}}
```
> Click <a href="https://github.com/besttime-app/slate/blob/master/source/examples/forecast_new/forecast_new_response.json" target="_blank">here</a> for the full JSON response


Endpoint
`https://BestTime.app/api/v1/forecast/new/`

### Create attributes

List forecast input attributes

### Response attributes

- **analysis** `object`  Containing the all the included analytics like 'peak_hours', 'busy_hours', etc.  
 
 - analysis.**day_info** `object`  
   Details about the day    
  &nbsp;
     - analysis.day_info.**day_int** `int`  
       Day integer range `0` (Monday) to `6` (Sunday)  
       &nbsp;
     - analysis.day_info.**day_rank_max** `int`  
       Day ranking based on maximum busyness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most busy day of the week.  
       &nbsp;
     - analysis.day_info.**day_rank_mean** `int`  
       Day ranking based on mean busyness of the day. Range `1` to `7`. E.g. `2` indicates the 2nd most busy day of the week.  
       &nbsp;
     - analysis.day_info.**day_text** `string`  
       Day name. E.g. `monday`  
       &nbsp;
     - analysis.day_info.**venue_closed** `int`  
       Hour of day when the venue closes. Range `0` to `23` hour  
       &nbsp;
 - analysis.**hour_analysis** `list`  
   List with hour objects, containing details per hour.  