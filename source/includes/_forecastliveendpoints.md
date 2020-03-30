

## Live forecast

> Create a Live forecast:

```python
import requests
import json

url = "https://BestTime.app/api/v1/forecast/live"

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
curl --location --request POST 'https://BestTime.app/api/v1/forecast/live' \
--header 'Content-Type: application/json' \
--data-raw '{
    "venue_name" : "McDonald'\''s",
	  "venue_address" : "1201 Ocean Ave, San Francisco, CA 94112, United States",
	  "api_key_private": "e267713ecda84c77a055294dbb12c6d4"
}	'
```

```javascript
var settings = {
  "url": "https://BestTime.app/api/v1/forecast/live",
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

The 'live forecast' endpoint is used to get live information of the venue. Life forecasts are either created using the venue name and address, or the venue_id as input in the request. The response includes information regarding the live busyness at this moment compared to the forecasted busyness of the corresponding hour.  

When creating a live forecast the normal forecast for the venue will also be updated, and saved on the server. The updated forecast will be available through the normal query endpoints. 


### Input attributes New Forecast

- **venue_name** `string` <span style="color:blue">OPTIONAL</span>  
 Name of the venue (public business). When then using the `venue_id` the `venue_name` and `venue_address` can be omitted.  
 &nbsp; 
- **venue_name** `string` <span style="color:blue">OPTIONAL</span>  
 Address of the venue (public business). The address does not have to be exact, but needs to be precise enough for the geocoder engine to find the correct venue. The more specific the address the higher chance the geocoder will find the venue. The response object will also display the `venue_name` and `venue_address`, but is using the name and address of the geocoder's found venue. Check the `venue_name` and `venue_address` in the response object to verify if the correct venue has been forecasted.  
 &nbsp;
- **venue_id** `string` <span style="color:blue">OPTIONAL</span>  
 The unique ID for the venue. The venue_id can be retrieved from a 'new forecast' endpoint response, or by the 'all venues' endpoint which shows all previously forecasted venues. To use the `venue_id` as input, the venue needs to be forecasted before. When the `venue_id` parameter is omitted the `venue_name` and `venue_address` parameters are required.  
 &nbsp; 
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-keys)  
 &nbsp; 

<aside class="notice">
New forecast endpoint: https://BestTime.app/api/v1/forecast/live
</aside>

<aside class="notice">
HTTP method: POST
</aside>

<aside class="warning">
The live forecast endpoint is only available for platinum subscribers.
</aside>


> The above request returns JSON structured like this:

```json
{
    "analysis": {
        "venue_forecasted_popularity": 28,
        "venue_live_forecasted_detla": -15,
        "venue_live_popularity": 13,
        "venue_live_popularity_available": true
    },
    "status": "OK",
    "venue_info": {
        "venue_current_gmttime": "Thu, 12 Mar 2020 13:05:53 GMT",
        "venue_current_localtime_iso": "2020-03-12T06:05:53.948572-07:00",
        "venue_id": "wqXCm8K8wr7DmcKTw4BsU8KWemrCo8KWdMOFw4TDhMKHwrDClFjChmHConHCsw==",
        "venue_name": "McDonald's",
        "venue_timezone": "America/Los_Angeles"
    }
}
```

### Response attributes Live Forecast <a name="responseattributesnewforecast"></a>

- **analysis** `list`  
 TODO
 List with an analysis object for each day of the week, containing analysis like 'peak_hours', 'busy_hours', etc per day. The list contains days `object` and are sorted on day of the week: `day_int` `0` (Monday) to `6` (Sunday).  
 &nbsp; 

 TODO



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
 - venue_info.**venue_current_gmtttime** `string`  
   Time at the venue in Greenwich Mean Time.  
 - venue_info.**venue_current_localtime_iso** `string`  
   Local time at the venue in ISO standard format.  
  &nbsp;
 - venue_info.**venue_timezone** `string`  
  The timezone of the venue. E.g. `America/Los Angeles`.  
  &nbsp;


TODO HTTP DELETE method forecast new 
  
TODO ADD Live forecast endpoint
