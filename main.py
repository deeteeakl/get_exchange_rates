import logging
import logging.handlers
import os

import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise

try:
    END_POINT = os.environ["END_POINT"]
    logger.info(f"end point : {END_POINT}")
except KeyError:
    logger.info("Endpoint not defined")
    #raise


if __name__ == "__main__":
    #logger.info(f"Token value: {SOME_SECRET}")

    r = requests.get('https://weather.talkpython.fm/api/weather/?city=Oxford&country=GB')
    if r.status_code == 200:
        data = r.json()
        temperature = data["forecast"]["temp"]
        logger.info(f'Weather in Oxford: {temperature}')

        my_json = {"message": temperature}
        r = requests.post("https://wytham.tk/api/webhook/webhook-test-ETDK-wfnUPlUbcVf2rM28yvz", json=my_json)