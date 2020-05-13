import logging

# https://docs.python.org/3/library/logging.html#logging.basicConfig

# logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

# logging.basicConfig(format='%(asctime)s - %(levelno)s - %(message)s', level=logging.INFO)

# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S') 




logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')


logging.info('Admin logged in')
