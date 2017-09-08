from lib import Logger
from app.Handlers import Touch, SDI

# Settings
i2c_addr_10 = 0x21
i2c_addr_20 = 0x22
i2c_addr_30 = 0x23
interval = 10

# Initialise and start the logger
logger = Logger.Logger(interval)
# logger.add_handler('touch', Touch.Handler(10, i2c_addr_10))
# logger.add_handler('touch', Touch.Handler(20, i2c_addr_20))
# logger.add_handler('touch', Touch.Handler(30, i2c_addr_30))
logger.add_handler('touch_sdi', SDI.Handler())
logger.start()