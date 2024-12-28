<?php

// sudo dapr run --app-id subscriber-app --app-port 3000 -- php subscriber.php

require_once('vendor/autoload.php');

$daprHost = 'http://localhost:3510';
$appId = 'subscriber-app';

// Funkcja do pobierania wiadomości
function getMessageFromDapr($daprHost, $appId)
{
    $url = "$daprHost/v1.0/invoke/$appId/method/get-message"; // Endpoint Dapr

    // Inicjalizacja klienta Guzzle
    $client = new GuzzleHttp\Client();

    try {
        // Wysyłanie żądania GET do Dapr
        $response = $client->request('GET', $url);
        $statusCode = $response->getStatusCode();
        $responseBody = $response->getBody()->getContents();

        echo "Status: $statusCode\n";
        echo "Odpowiedź: $responseBody\n";
    } catch (Exception $e) {
        echo "Błąd: " . $e->getMessage() . "\n";
    }
}

// Wywołanie funkcji
getMessageFromDapr($daprHost, $appId);
