import logging

fmt_str = '%(asctime)s:%(name)s:%(levelname)s:%(process)s:%(filename)s:%(message)s'

logging.basicConfig(level=logging.DEBUG, format=fmt_str, filename='error.log')
logging.debug('debug message')

logging.info('confirmation note')
logging.warning('warning message')
logging.error('an error note')
logging.critical('panic error')