<?php

// Example 1: cURL
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => 'https://besttime.app/api/v1/forecasts?venue_name=Central%20Park&venue_address=NYC,%20USA&api_key_private=pri_XXXXXXXXXXXXXXXXXX',
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => '',
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => 'POST',
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;


// Example 2: Guzzle
$client = new Client();
$body = '';
$request = new Request('POST', 'https://besttime.app/api/v1/forecasts?venue_name=Central Park&venue_address=NYC, USA&api_key_private=pri_XXXXXXXXXXXXXXXXXX', [], $body);
$res = $client->sendAsync($request)->wait();
echo $res->getBody();

// Example 3: HTTP_Request2

require_once 'HTTP/Request2.php';
$request = new HTTP_Request2();
$request->setUrl('https://besttime.app/api/v1/forecasts?venue_name=Central Park&venue_address=NYC, USA&api_key_private=pri_XXXXXXXXXXXXXXXXXX');
$request->setMethod(HTTP_Request2::METHOD_POST);
$request->setConfig(array(
  'follow_redirects' => TRUE
));
$request->setBody('');
try {
  $response = $request->send();
  if ($response->getStatus() == 200) {
    echo $response->getBody();
  }
  else {
    echo 'Unexpected HTTP status: ' . $response->getStatus() . ' ' .
    $response->getReasonPhrase();
  }
}
catch(HTTP_Request2_Exception $e) {
  echo 'Error: ' . $e->getMessage();
}

// Examle 4: PeCL_http

$client = new http\Client;
$request = new http\Client\Request;
$request->setRequestUrl('https://besttime.app/api/v1/forecasts?venue_name=Central Park&venue_address=NYC, USA&api_key_private=pri_XXXXXXXXXXXXXXXXXX');
$request->setRequestMethod('POST');
$body = new http\Message\Body;
$request->setBody($body);
$request->setOptions(array());

$client->enqueue($request)->send();
$response = $client->getResponse();
echo $response->getBody();
