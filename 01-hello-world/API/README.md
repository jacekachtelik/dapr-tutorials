# Wykorzystanie Dapr API

W tym przewodniku za pomocą API nastąpi:

- Zapisanie stanu 
- Odczyt stanu
- Usunięcie stanu


### 1. Uruchomienie aplikacji z Dapr sidecar

Polecenie:

```bash
sudo dapr run --app-id myapp --dapr-http-port 3500
```
uruchomi aplikację (pustą) o nazwie **myapp**.

### 2. Zapisanie stanu

Zapisanie stanu:
```json
[
    {
        "key": "Powitanie",
        "value": "Witaj świecie"
    }
]
```

następuje komendą:
```bash
curl -X POST -H "Content-Type: application/json" -d '[{ "key": "Powitanie", "message": "Witaj świecie"}]' http://localhost:3500/v1.0/state/statestore
```
Otrzymujemy kod (widoczny w Postman): **204 No content**

### 2. Pobranie stanu

Pobranie stanu można wykonać komendą:

```bash
curl --location 'http://localhost:3500/v1.0/state/statestore/Powitanie'
```


### 3. Weryfikacja, w jaki sposób dane są zapisywane

Stan zapisywany jest w Redisie. Należy wejść do kontenera Redis-a.
```bash
sudo docker exec -it dapr_redis redis-cli
```

Po wejściu do kontenenera, w konsoli nalezy wprowadzić komendę:
```bash
keys *
```

Oczekiwany rezultat:
```bash
1) "myapp||Powitanie"
```

Wartość może zostać podejrzana komendą:

```bash
hgetall "myapp||Powitanie"
```

Wynik:

```bash
1) "data"
2) "\"Witaj \xc5\x9bwiecie\""
3) "version"
4) "2"
```

Wyjście z konsoli:
```bash
exit
```

### 4.  Usunięcie stanu

```bash
curl -v -X DELETE -H "Content-Type: application/json" http://localhost:3500/v1.0/state/statestore/Powitanie
```