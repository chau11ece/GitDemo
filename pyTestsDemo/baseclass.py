import inspect
import logging


class BaseClass:
    def get_logger(self):
        # create logger
        logger_name = inspect.stack()[1][3]
        # logger = logging.getLogger(__name__)
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        # create console handler and set level to DEBUG
        file_handler = logging.FileHandler('logfile.log')
        file_handler.setLevel(logging.DEBUG)

        # create formatter
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")

        # add formatter to ch
        file_handler.setFormatter(formatter)

        # add ch to logger
        logger.addHandler(file_handler)  # handler object

        return logger
