import logging, logging.handlers

def get_logger(module_name):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s: %(levelname)s : %(message)s', '%m/%d/%Y %I:%M:%S %p')
    file_handler = logging.FileHandler('logs/automation_test.log', mode='w')
    file_handler.setFormatter(formatter)

    if(logger.hasHandlers()):
        logger.handlers.clear()
    logger.addHandler(file_handler)
    return logger

# logging.basicConfig(filename='automation_test.log', filemode='w+', format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)