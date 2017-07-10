import time
from lib import InfluxAdapter

class Logger:
  interval = 60
  active = False
  handlers = {}

  def __init__(self, interval = 60):
    self.interval = interval

  def add_handler(self, name, handler):
    self.handlers[name] = handler

  def start(self):
    self.active = True
    while self.active:
      for name, handler in self.handlers.iteritems():
        fields = handler()
        if fields:
          InfluxAdapter.write(name, fields)
      time.sleep(self.interval)

  def stop(self):
    self.active = False