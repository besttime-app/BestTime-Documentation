
## Query now

> Query the now:

```python
import requests
import json

url = "https://besttime.app/api/v1/forecasts/now"

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
curl --location --request GET 'https://besttime.app/api/v1/forecasts/now?api_key_public=pub_e11661721b084d36b8f469a2c012e754&venue_id=ven_51387131543761435650505241346a394a6432395362654a496843'
```

```javascript
var params = {
    'api_key_public': 'pub_e11661721b084d36b8f469a2c012e754',
    'venue_id': 'ven_51387131543761435650505241346a394a6432395362654a496843'
}

$.ajax({
"url": "https://besttime.app/api/v1/forecasts/now?" + new URLSearchParams(params),
"method": "GET"
}).done(function (response) {
    console.log(response);
});
```

### Input attributes Query Now

The 'query now' endpoint is used to retrieve the 'hour analysis' forecast for the current hour. The hour is the venues current hour with the local timezone taken into account.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-keys)  
 &nbsp; 
- **hour_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the hour (hour of the venue in the local timezone). E.g. `0` means current hour, and `-2` means two hours ago. Range: min `-12`, max `12`.  
 &nbsp; 

<aside class="notice">
Query current hour endpoint: https://BestTime.app/api/v1/forecasts/now
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
        "venue_name": "McDonald's"
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

