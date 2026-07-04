import logging
import os
from datetime import datetime


class Logger:

    _logger = None

    @classmethod
    def get_logger(cls):

        if cls._logger:
            return cls._logger

        os.makedirs("logs", exist_ok=True)

        filename = datetime.now().strftime("%Y-%m-%d_%H-%M-%S.log")

        logfile = os.path.join("logs", filename)

        logger = logging.getLogger("LeadGenPro")

        logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        # File
        file_handler = logging.FileHandler(logfile)

        file_handler.setFormatter(formatter)

        # Console
        console_handler = logging.StreamHandler()

        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        cls._logger = logger

        return logger