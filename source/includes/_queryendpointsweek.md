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
