# 02. Service Invocation

Niniejszy przykład pokazuje metodę na wywołanie usługi przez inną usługę przekazując przez REST API wiadomość.
Przekazanie wykorzystuje dapr-a.

![Schemat poglądowy działania](__media/dapr-service-invocation.png)

Poniższy przykład jest następujący

## Uruchomienie: 

```bash
sudo dapr run  --app-id publisher --app-protocol http --dapr-http-port 3500 -- ./pub_sub/bin/python3 app.py
```