from random import randint
from random import seed

import logging
import logging.config
import yaml

with open('config_pas7b.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

logger = logging.getLogger(__name__)

# logger.debug('This is a debug message')
# logger.info('This is an info message')
# logger.warning('This is a warning message')
# logger.error('This is an error message')
# logger.critical('This is a critical message')


# generate random integer values
# seed random number generator
seed(1)

while True:
    value = randint(0, 10)
    logger.error(f"Generated Error{str(value)}")
    logger.warning(f"Generated Waring{str(value)}")
else:
    pass
