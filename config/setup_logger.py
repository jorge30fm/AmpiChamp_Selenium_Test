import logging, logging.handlers, datetime

def get_logger(module_name):
    '''sets up the log file for the test, log file created in logs folder and named based on timestamp'''

    #name file with timestamp
    log_file_name = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S' + '.log')

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    #format log output
    formatter = logging.Formatter('%(asctime)s: %(levelname)s : %(message)s', '%m/%d/%Y %I:%M:%S %p')
    file_handler = logging.FileHandler('logs/' + log_file_name, mode='w')
    file_handler.setFormatter(formatter)

    if(logger.hasHandlers()):
        logger.handlers.clear()
    logger.addHandler(file_handler)
    return logger
