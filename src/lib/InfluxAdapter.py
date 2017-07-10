from influxdb import InfluxDBClient
import time

# Don't consume directly, use the get_adapter method
influx = None

# Settings
influx_host = "localhost"
influx_port = 8086
influx_user = "admin"
influx_password = "admin"
influx_dbname = "Logger"

# Get or create the InfluxDB object
def get_adapter():
  global influx
  if (influx is None):
    influx = InfluxDBClient(influx_host, influx_port, influx_user, influx_password, influx_dbname)
  return influx

# Write to influx
def write(measurement, fields, tags = {}):
  iso = time.ctime()
  json_body = [{
    "measurement": measurement,
    "tags": tags,
    "time": iso,
    "fields": fields
  }]
  get_adapter().write_points(json_body)