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