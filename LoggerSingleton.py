import logging

class LoggerSingleton:
    _instance = None

    def __new__(cls): # LoggerSingleton()
        if cls._instance is None:
            logging.basicConfig(filename='myapp.log', level=logging.DEBUG)
            cls._instance = logging.getLogger(__name__)
        return cls._instance
    
    def info(self, message):
        self._instance.info(message)

    def debug(self, message):
        self._instance.debug(message)

    def warning(self, message):
        self._instance.warning(message)

if __name__ == '__main__':
    logger = LoggerSingleton()
    logger.info("Hello")