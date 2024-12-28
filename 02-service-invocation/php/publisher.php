<?php

require_once 'vendor/autoload.php';


use GuzzleHttp\Client;
use GuzzleHttp\Exception\RequestException;


$client = new Client();

$data = [
    'documentId' => date('YmdHis'),
];

$headers = [
    'Content-Type'  =>  'application/json',
    'dapr-app-id'   =>  'subscriber-app'
];

try {

    $response = $client->post('http://localhost:3510/documents', [
        'json'      =>  $data,
        'headers'   =>  $headers,
    ]);

    $statusCode = $response->getStatusCode();
    $responseBody = $response->getBody()->getContents();

    echo "Wiadomość wysłana! Status: $statusCode\n";
    echo "Odpowiedź: $responseBody\n";
} catch (RequestException $e) {
    echo "Błąd: " . $e->getMessage() . "\n";
}

// Uruchomienie: php publisher.php 
// lub z wykorzystaniem dapr-a
// sudo dapr run --app-id publisher-app --app-protocol http --dapr-http-port 3515 -- php publisher.php