import logging


class MyLogger(logging.getLoggerClass()):
    # ... override behaviour here
    FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
    logging.basicConfig(format=FORMAT)
    d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
    logging.warning('Protocol problem: %s', 'connection reset', extra=d)