import datetime
from lib.I2CMoistureSensor import Sensor

def Handler(depth, address):
  class context:
    chirp = None

  def handler():
    if (context.chirp is None):
      context.chirp = Sensor(1, address)

    try:
      capacitance = context.chirp.moist()
      temperature = context.chirp.temp()
      print "%s\t%d\t\t%d" % (str(datetime.datetime.now()), capacitance, temperature)

      fields = {
        ("capacitance_" + str(depth)): capacitance,
        ("temperature_" + str(depth)): temperature
      }
      return fields

    except IOError:
      context.chirp = None

  return handler