# Observability Stack for Raspberry Pi with BME680 Sensor
This project implements a complete observability stack for a Raspberry Pi Zero with a BME680 environmental sensor. The architecture collects environmental data (temperature, humidity, pressure, gas resistance), exposes it via Prometheus metrics, and visualizes it using Grafana dashboards.
## Architecture Overview
```
+-------------------+        +-------------------+        +-------------------+
|   Raspberry Pi    |        |  Docker Desktop   |        |     Grafana       |
|  Zero + BME680    |        |                   |        |                   |
|                   |        |                   |        |  +--------------+ |
|  +--------------+ |        |  +--------------+ |        |  |              | |
|  |Python Script | |        |  |              | |        |  |  Dashboards  | |
|  |  (Metrics    | |        |  |  Prometheus  | |        |  |              | |
|  |   Exporter)  | |------->|  |  (Storage)   |--------->|  |              | |
|  |              | |  Pull  |  |              | |  Query |  |              | |
|  +--------------+ |        |  +--------------+ |        |  +--------------+ |
|                   |        |                   |        |                   |
|                   |        |  +--------------+ |        |                   |
|                   |        |  |              | |        |                   |
|                   |        |  |     Loki     | |        |                   |
|                   |------->|  |  (Log Agg.)  |--------->|                   |
|                   |  Push  |  |              | |  Query |                   |
+-------------------+        |  +--------------+ |        +-------------------+
                             |                   |
                             +-------------------+
```


### installation
telegraf 

/etc/telegraf/telegraf.d/bme680.conf
```
sudo cp bme680.conf /etc/telegraf/telegraf.d/
sudo chown telegraf:telegraf /etc/telegraf/telegraf.d/bme680.conf
sudo chmod 644 /etc/telegraf/telegraf.d/bme680.conf
sudo telegraf -config /etc/telegraf/telegraf.d/bme680.conf -test
sudo systemctl start telegraf
sudo journalctl -u telegraf -f # if error
```

if modif .conf
```
sudo systemctl daemon-reload
sudo systemctl restart telegraf
```

```
http://raspberrypigarden.local:9273/metrics
```