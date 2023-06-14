import click
import logging
import datetime as dt

from utils import *
from config import LOGGER


# get datetime
today = dt.datetime.today()
filename =  f"{today.year}-{today.month:02d}-{today.day:02d} {today.hour:02d}h{today.minute:02d}m{today.second:02d}s.log"


# setup logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(LOGGER.LOGGER_NAME)
logger.propagate = False \
formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(filename)s] %(message)s', "%Y-%m-%d %H:%M:%S")


# set up log file and LOGFILE handler & attach handler
file_handler = logging.FileHandler(filename)
# file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


# format log on console & attach handler
stream_handler = logging.StreamHandler()
# stream_handler.setLevel(logging.DEBUG)
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)





def A_all():
    A1()
    A2()
    A3()


def A_some():
    A1()
    A3()


def B_all():
    B1()
    B2()
    

def C_all():
    C1()
    C1()
    C1()


def all_alpha():
    A1()
    A2()
    A3()
    B1()
    B2()
    C1()


@click.group()
def A():
    logger.info("AAAAA")


@click.group()
def B():
    logger.info("BBBBBB")


@click.group()
def C():
    logger.info("CCCCCCC")


@click.group()
def ALL():
    logger.info("ALLLL")


@click.group()
def main():
    pass


A.command(A_all)
A.command(A_some)
B.command(B_all)
C.command(C_all)
ALL.command(all_alpha)

main.add_command(ALL)
main.add_command(A)
main.add_command(B)
main.add_command(C)


if __name__ == "__main__":
    main()



# Example code to put in console:
# python run.py all all-alpha
# python run.py a a-all
# python run.py a a-some
# python run.py b b-all
