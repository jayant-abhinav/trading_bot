import logging
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(
    LOG_DIR,
    "trading_bot.log"
)

logger = logging.getLogger(
    "TradingBot"
)

logger.setLevel(logging.INFO)

logger.propagate = False

file_handler = logging.FileHandler(
    LOG_FILE
)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s"
)

file_handler.setFormatter(
    formatter
)

if not logger.handlers:
    logger.addHandler(file_handler)