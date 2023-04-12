"""Logging configuration."""

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("./logs/info.log"),
        logging.StreamHandler()
    ]
)

log = logging.getLogger('')
