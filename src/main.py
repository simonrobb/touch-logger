import time
import datetime
from influxdb import InfluxDBClient
from Sensor import Sensor

# Settings
addr = 0x21
host = "localhost"
port = 8086
user = "admin"
password = "admin"
dbname = "Logger"

# Connect to the sensor
sensor = Sensor(1, addr)

# Create the InfluxDB object
influx = InfluxDBClient(host, port, user, password, dbname)

print "Timestamp\t\t\tMoisture\tTemperature"
while True:
  capacitance = sensor.moist()
  temperature = sensor.temp()
  iso = time.ctime()

  print "%s\t%d\t\t%d" % (str(datetime.datetime.now()), capacitance, temperature)
  json_body = [{
    "measurement": "sensor",
    "tags": {},
    "time": iso,
    "fields": {
      "capacitance_1": capacitance,
      "temperature": temperature
    }
  }]
  influx.write_points(json_body)
  time.sleep(10)