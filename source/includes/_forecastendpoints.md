
# Forecasts endpoints

> Create a new forecast:

```python
import requests
import json

url = "https://BestTime.app/api/v1/"

headers = {
    'Content-Type': 'application/json'
}

payload = json.dumps({
    'api_key_private': 'e267713ecda84c77a055294dbb12c6d4'
})

response = requests.request("POST", url, headers=headers, data = payload)

response_dict = json.loads(response.text.encode('utf8'))
```

```shell
# cURL
curl --location --request POST 'https://BestTime.app/api/v1/' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key_private": "e267713ecda84c77a055294dbb12c6d4"
}	'
```

```javascript
var settings = {
  "url": "https://BestTime.app/api/v1/",
  "method": "POST",
  "headers": {
    "Content-Type": "application/json"
  },
  "data": JSON.stringify({
    "api_key_private":"e267713ecda84c77a055294dbb12c6d4"
    }),
};

$.ajax(settings).done(function (response) {
  console.log(response);
});
```


> The above command returns JSON structured like this:

```json
  {
    'status' : 'OK',
    'message' : 'Valid api_key_private',
    'valid': true,
    'quota_forecasts_remaining' : 300,
    'quota_queries_remaining' : 1000000
  }
```
> Click <a href="http://example.com/" target="_blank">here</a> for the full JSON response


