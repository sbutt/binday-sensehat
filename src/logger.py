# src/logger.py

import logging
from logging.handlers import RotatingFileHandler
import os

# =====================================================

def setup_logger():

    os.makedirs("logs", exist_ok=True)

    logger = logging.getLogger("binday")

    logger.setLevel(logging.INFO)

    if logger.handlers:
        return logger

    handler = RotatingFileHandler(
        "logs/binday.log",
        maxBytes=500000,
        backupCount=3
    )

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger
