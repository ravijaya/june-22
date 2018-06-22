from pscustomlogutils import epsilon
from time import sleep

for item in range(1, 10):
    sleep(1)
    epsilon.debug('a sample debug messsae  {}'.format(item))

