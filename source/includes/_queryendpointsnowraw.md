## Query now raw

> Query the raw hour data for current hour:

```python
import requests
import json

url = "https://besttime.app/api/v1/forecasts/now/raw"

params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
}

response = requests.request("GET", url, params=params)

data = json.loads(response.text)

print(data)
```

```shell
# cURL
curl --location --request GET 'https://besttime.app/api/v1/forecasts/now/raw?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843'
```

```javascript
var params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
}

$.ajax({
"url": "https://besttime.app/api/v1/forecasts/now/raw?" + new URLSearchParams(params),
"method": "GET"
}).done(function (response) {
    console.log(response);
});
```

### Input attributes

The 'query now raw' endpoint is used to retrieve the raw data from an existing forecast for one hour of the day. It automatically determines the current day and hour in the local timezone of the venue.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **day_int** `int` <span style="color:orange">REQUIRED</span>  
 Day of the week. Range `0` (Monday) to `6` (Sunday).  
 &nbsp;

<aside class="notice">
Now raw endpoint: https://BestTime.app/api/v1/forecasts/now/raw
</aside>

<aside class="notice">
HTTP method: GET
</aside>

<aside class="warning">
The now raw endpoint is only available for platinum subscribers.
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

