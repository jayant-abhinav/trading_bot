from bot.client import get_client
from bot.logging_config import logger
import time

client = get_client()


def place_market_order(symbol, side, quantity):
    try:
        logger.info(
            f"MARKET REQUEST | "
            f"symbol={symbol}, "
            f"side={side}, "
            f"quantity={quantity}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="MARKET",
            quantity=quantity
        )

        # Give Binance a moment to process
        time.sleep(1)

        order_details = client.futures_get_order(
            symbol=symbol,
            orderId=response["orderId"]
        )

        logger.info(
            f"MARKET RESPONSE | {order_details}"
        )

        return order_details

    except Exception:
        logger.exception("MARKET ORDER FAILED.")
        raise


def place_limit_order(symbol, side, quantity, price):
    try:
        logger.info(
            f"LIMIT REQUEST | "
            f"symbol={symbol}, "
            f"side={side}, "
            f"quantity={quantity}, "
            f"price={price}"
        )

        response = client.futures_create_order(
            symbol=symbol,
            side=side,
            type="LIMIT",
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(
            f"LIMIT RESPONSE | {response}"
        )

        return response

    except Exception:
        logger.exception("LIMIT ORDER FAILED.")
        raise