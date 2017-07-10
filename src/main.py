import time
import datetime
from lib import Logger
from Sensor import Sensor

# Settings
i2c_addr = 0x20
interval = 10

logger = Logger.Logger(interval)
sensor = None

# Take an I2C sample
def sample():
  global sensor
  if (sensor is None):
    sensor = Sensor(1, i2c_addr)

  try:
    capacitance = sensor.moist()
    temperature = sensor.temp()
    print "%s\t%d\t\t%d" % (str(datetime.datetime.now()), capacitance, temperature)

    fields = {
      "capacitance_1": capacitance,
      "temperature": temperature
    }
    return fields

  except IOError:
    sensor = None

# Start the logger
print "Timestamp\t\t\tMoisture\tTemperature"
logger.add_handler('sensor', sample)
logger.start()