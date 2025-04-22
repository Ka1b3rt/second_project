import logging
import sys


def setup_logging(level=logging.INFO):
    fmt = "%(levelname)s (%(asctime)s) %(message)s (Line: %(lineno)s) %(filename)s"
    date_fmt = "%d/%m/%Y %I:%M:%S"

    logging.basicConfig(stream=sys.stdout, level=level, format=fmt, datefmt=date_fmt)
