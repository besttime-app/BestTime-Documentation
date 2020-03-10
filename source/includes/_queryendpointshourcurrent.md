
## Query current hour

> Query the current hour:

```python
import requests
import json

url = "https://BestTime.app/api/v1/query/now/"

headers = {
    'Content-Type': 'application/json'
}

payload = json.dumps({
    "api_key_public": "352a9addc0ac4c599572e56f504080d3",
	  "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
    "day_int": 3,
    "hour": 23
})

response = requests.request("POST", url, headers=headers, data = payload)

response_dict = json.loads(response.text.encode('utf8'))
```

```shell
# cURL
curl --location --request POST 'https://BestTime.app/api/v1/query/now/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key_public": "352a9addc0ac4c599572e56f504080d3",
	"venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
  "day_int": 3,
  "hour": 23
}	'
```

```javascript
var settings = {
  "url": "https://BestTime.app/api/v1/query/now/",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    	"api_key_public": "352a9addc0ac4c599572e56f504080d3",
	    "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
      "day_int": 3,
      "hour": 23
    }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```

### Input attributes Query Current Hour

The 'query current hour' endpoint is used to retrieve the 'hour analysis' forecast for the current hour. The hour is the venues current hour with the local timezone taken into account.

- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'forecast list' endpoint which shows all previously forecasted venues.  
 &nbsp; 
- **api_key_public** `string` <span style="color:orange">REQUIRED</span>  
 Public API Key. See more info on [API keys](#api-keys)  
 &nbsp; 
- **hour_step** `int` <span style="color:blue">OPTIONAL</span>  
  Adjust the hour (hour of the venue in the local timezone). E.g. `0` means current hour, and `-2` means two hours ago. Range: min `-12`, max `12`.  
 &nbsp; 

<aside class="notice">
Query current hour endpoint: https://BestTime.app/api/v1/query/hour/
</aside>

<aside class="notice">
HTTP method: POST
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
        "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
        "venue_name": "McDonald's"
    }
}
```

> Click <a href="https://github.com/besttime-app/slate/blob/master/source/examples/query_hour/query_hour_response.json" target="_blank">here</a> for the raw JSON response.

### Response attributes Query Current Hour

The response attributes are exactly the same as the attributes in the 'query hour' endpoint.
See [query hour](#query-hour) reponse attributes.
