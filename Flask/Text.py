import logging
logging.basicConfig(filename='api_logs.txt',level=logging.INFO)


logging.info('API REQUEST RECEIVED...')
logging.error('Error in processing API request....')
logging.debug('Debugging request data....')