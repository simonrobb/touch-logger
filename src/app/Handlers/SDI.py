import time
import serial

def Handler():
  class context:
    sensor = None

  def sendCommand(command):
    sdi.write(command)
    response = ''
    lastEvent = time.time()
    while ((time.time() - lastEvent)<0.023):
      c = sdi.read()
      if (c):
        response += c
        lastEvent = time.time()
    return response

  def handler():
    if (context.sensor is None):
      context.sensor = serial.Serial("/dev/serial0", baudrate=9600, timeout=1.0)
      time.sleep(5)

    try:
      # Take reading
      sendCommand('0M!')

      # Get results of reading
      # context.sensor.write('0D0!')
      # moistures = result[2:29].split('+')

      # Get results of reading
      # context.sensor.write('0D0!')
      # result = context.sensor.read(32)
      # temperatures = result[2:29].split('+')

      # fields = {
      #   "moisture_1": float(moistures[0]),
      #   "moisture_2": float(moistures[1]),
      #   "moisture_3": float(moistures[2]),
      #   "moisture_4": float(moistures[3]),
      #   "temperature_1": float(temperatures[0]),
      #   "temperature_2": float(temperatures[1]),
      #   "temperature_3": float(temperatures[2]),
      #   "temperature_4": float(temperatures[3])
      # }
      # return fields

    except IOError:
      context.sensor = None

  return handler