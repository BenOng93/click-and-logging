import logging
from config import LOGGER

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(LOGGER.LOGGER_NAME)


def A1():
    logger.info("A1")

def A2():
    logger.info("A2")

def A3():
    logger.info("A3")

def B1():
    logger.info("B1")

def B2():
    logger.info("B2")

def C1():
    logger.info("C1")


