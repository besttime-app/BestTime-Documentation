# Venue collections

Collections can be used to group venues together. Each collection has an unique 36 `collection_id` and an optional name.
Venues inside a collection are managed using the `venue_id` of each venue. 
Your existing collections can be also viewed on the [Collection page](https://beta.besttime.app/api/v1/collection_list). On the page, click on a collection_id to see which venues are inside or to open the collection in the Radar tool.

Through the collections API endpoints you can create or delete collections, and add or remove venues to/from an existing collection. 

There are multiple ways to use a collection in combination with the other BestTime tools/ API endpoints 
- Manually add venues to a collection to group them and later call the collection to simply know which `venue_id`’s belong together.
- Pass a collection_id to a [New forecast](#new-foot-traffic-forecast) to automatically add one or multiple successful venues to an existing collection. 
- The Radar tool and Venue Filter accepts a collection_id as input show and filter only on the venues inside that collection
- The Venue Search tool and API endpoint automatically creates a new collection with a new search query, with the search query as collection name. The Venue Search API endpoint also accepts an existing collection id. This will merge the new search results with the given collection.

## Create a collection

```python
import requests
import json

url = "https://beta.besttime.app/api/v1/collection"

params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
    'collection_id': 'col_51387131543761435650505241346a39',
    'name': 'Supermarkets in Los Angeles, CA'
}

response = requests.request("POST", url, params=params)

data = json.loads(response.text)

print(data)
```

```shell
# cURL
curl --location --request POST 'https://beta.besttime.app/api/v1/collection?api_key_private=pri_s43661721b084d36b8f469a2c012e754&
collection_id=col_51387131543761435650505241346a39&
name=Supermarkets%20in%20Los%20Angeles%20CA'
```

```javascript
var params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
    'collection_id': 'col_51387131543761435650505241346a39',
    'name': 'Supermarkets in Los Angeles, CA'
}

$.ajax({
"url": "https://beta.besttime.app/api/v1/collection?" + new URLSearchParams(params),
"method": "POST"
}).done(function (response) {
    console.log(response);
});
```

### Input attributes

- **collection_id** `string` <span style="color:blue">OPTIONAL</span>  
 The unique ID for the collection, 36 characters long. A new unique `collection_id` will be generated if no self generated id is included in the request.
 &nbsp; 
- **name** `string` <span style="color:blue">OPTIONAL</span>  
 Name for the collection. Does not have to be unique. Maximum `128` characters long.
 &nbsp; 
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-keys)  
 &nbsp; 

<aside class="notice">
Collection create endpoint: https://beta.besttime.app/api/v1/collection
</aside>

<aside class="notice">
HTTP method: POST
</aside>


> The above request returns JSON structured like this:

```json
{
    "collection": {
        "api_key_private": "pri_s43661721b084d36b8f469a2c012e754",
        "collection_id": "col_51387131543761435650505241346a39",
        "name": "Supermarkets in Los Angeles, CA"
    },
    "status": "OK"
}
```


## Add venues to a collection

```python
import requests
import json

url = "https://beta.besttime.app/api/v1/collection/col_51387131543761435650505241346a39/ven_51387131543761435650505241346a394a6432395362654a496843"

params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
}

response = requests.request("POST", url, params=params)

data = json.loads(response.text)

print(data)
```

```shell
# cURL
curl --location --request POST 'https://beta.besttime.app/api/v1/collection/col_51387131543761435650505241346a39/ven_51387131543761435650505241346a394a6432395362654a496843?api_key_private=pri_s43661721b084d36b8f469a2c012e754
```

```javascript
var params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754'
}

$.ajax({
"url": "https://beta.besttime.app/api/v1/collection/col_51387131543761435650505241346a39/ven_51387131543761435650505241346a394a6432395362654a496843?" + new URLSearchParams(params),
"method": "POST"
}).done(function (response) {
    console.log(response);
});
```

### Input attributes

- **collection_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the collection, 36 characters long.
 &nbsp; 
- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 ID of the venue to be added to the collection.
 &nbsp; 
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-keys)  
 &nbsp; 

<aside class="notice">
Collection Add Venue endpoint: https://beta.besttime.app/api/v1/collection/{{collection_id}}/{{venue_id}}
</aside>

<aside class="notice">
HTTP method: POST
</aside>


> The above request returns JSON structured like this:

```json
{
    "collection_id": "col_51387131543761435650505241346a39",
    "message": "Venue added to collection",
    "status": "OK",
    "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843"
}
```

## Collection Venues

Returns a list with all venue_id's of venues in the collection

```python
import requests
import json

url = "https://beta.besttime.app/api/v1/collection/col_51387131543761435650505241346a39

params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
}

response = requests.request("GET", url, params=params)

data = json.loads(response.text)

print(data)
```

```shell
# cURL
curl --location --request GET 'https://beta.besttime.app/api/v1/collection/col_51387131543761435650505241346a39?api_key_private=pri_s43661721b084d36b8f469a2c012e754
```

```javascript
var params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754'
}

$.ajax({
"url": "https://beta.besttime.app/api/v1/collection/col_51387131543761435650505241346a39?" + new URLSearchParams(params),
"method": "GET"
}).done(function (response) {
    console.log(response);
});
```

### Input attributes

- **collection_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the collection, 36 characters long.
 &nbsp; 
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-keys)  
 &nbsp; 

<aside class="notice">
Collection Venues endpoint: https://beta.besttime.app/api/v1/collection/{{collection_id}}
</aside>

<aside class="notice">
HTTP method: GET
</aside>


> The above request returns JSON structured like this:

```json
{
    "collection_id": "col_51387131543761435650505241346a39",
    "status": "OK",
    "venue_ids": [
        "ven_51387131543761435650505241346a394a6432395362654a496843"
    ]
}
```

## Collection Remove venue

Removes a venue from the collection using the `venue_id`.

```python
import requests
import json

url = "https://beta.besttime.app/api/v1/collection/col_51387131543761435650505241346a39/ven_51387131543761435650505241346a394a6432395362654a496843"

params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
}

response = requests.request("DELETE", url, params=params)

data = json.loads(response.text)

print(data)
```

```shell
# cURL
curl --location --request DELETE 'https://beta.besttime.app/api/v1/collection/col_51387131543761435650505241346a39/ven_51387131543761435650505241346a394a6432395362654a496843?api_key_private=pri_s43661721b084d36b8f469a2c012e754
```

```javascript
var params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754'
}

$.ajax({
"url": "https://beta.besttime.app/api/v1/collection/col_51387131543761435650505241346a39/ven_51387131543761435650505241346a394a6432395362654a496843?" + new URLSearchParams(params),
"method": "DELETE"
}).done(function (response) {
    console.log(response);
});
```

### Input attributes

- **collection_id** `string` <span style="color:orange">REQUIRED</span>  
 The unique ID for the collection, 36 characters long.
 &nbsp; 
- **venue_id** `string` <span style="color:orange">REQUIRED</span>  
 ID of the venue to be removed from the collection.
 &nbsp; 
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-keys)  
 &nbsp; 

<aside class="notice">
Collection Remove Venue endpoint: https://beta.besttime.app/api/v1/collection/{{collection_id}}/{{venue_id}}
</aside>

<aside class="notice">
HTTP method: DELETE
</aside>


> The above request returns JSON structured like this:

```json
{
    "collection_id": "col_51387131543761435650505241346a39",
    "message": "Venue deleted from collection",
    "status": "OK",
    "venue_id": "ven_51387131543761435650505241346a394a6432395362654a496843"
}
```


## Collection delete

Delete a collection using the `collection_id`. Deleting a collection does not affect the venues listed in the collection itself.


```python
import requests
import json

url = "https://beta.besttime.app/api/v1/collection"

params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
    'collection_id': 'col_51387131543761435650505241346a39',
}

response = requests.request("DELETE", url, params=params)

data = json.loads(response.text)

print(data)
```

```shell
# cURL
curl --location --request DELETE 'https://beta.besttime.app/api/v1/collection?api_key_private=pri_s43661721b084d36b8f469a2c012e754&
collection_id=col_51387131543761435650505241346a39'
```

```javascript
var params = {
    'api_key_private': 'pri_s43661721b084d36b8f469a2c012e754',
    'collection_id': 'col_51387131543761435650505241346a39'
    }

$.ajax({
"url": "https://beta.besttime.app/api/v1/collection?" + new URLSearchParams(params),
"method": "DELETE"
}).done(function (response) {
    console.log(response);
});
```

### Input attributes

- **collection_id** `string` <span style="color:blue">OPTIONAL</span>  
 The unique ID for the collection, 36 characters long. 
 &nbsp; 
- **api_key_private** `string` <span style="color:orange">REQUIRED</span>  
 Private API Key. See more info on [API keys](#api-keys)  
 &nbsp; 

<aside class="notice">
Collection Delete endpoint: https://beta.besttime.app/api/v1/collection/{{collection_id}}
</aside>

<aside class="notice">
HTTP method: DELETE
</aside>

> The above request returns JSON structured like this:

```json
{
    "message": "collection_id col_51387131543761435650505241346a39 deleted",
    "status": "OK"
}
```

