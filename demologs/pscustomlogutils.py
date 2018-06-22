import logging
from logging.handlers import RotatingFileHandler

fmt_str = '%(asctime)s:%(name)s:%(levelname)s:%(process)s:%(filename)s:%(message)s'
fmt = logging.Formatter(fmt_str)  # what to log

rfh = RotatingFileHandler('access.log', maxBytes=32, backupCount=5)  # where to log
rfh.setFormatter(fmt)

epsilon = logging.getLogger('epsilon')
epsilon.setLevel(logging.DEBUG)
epsilon.addHandler(rfh)
