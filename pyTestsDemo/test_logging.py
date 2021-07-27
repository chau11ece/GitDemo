import logging


def test_logging():
    logger = logging.getLogger(__name__)

    file_handler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)  # filehandler object

    # 'application' code
    logger.setLevel(logging.DEBUG)
    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning mode")
    logger.error("A Major error has happened")
    logger.critical("Critical issue")
