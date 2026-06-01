import argparse
from bot.orders import place_market_order,place_limit_order

from bot.validators import(validate_symbol, validate_side,
    validate_order_type, validate_quantity, validate_price
)

from bot.logging_config import logger

def print_response(response):

    print("\n===== ORDER RESPONSE =====")

    print(
        f"Order ID      : "
        f"{response.get('orderId')}"
    )

    print(
        f"Status        : "
        f"{response.get('status')}"
    )

    print(
        f"Executed Qty  : "
        f"{response.get('executedQty')}"
    )

    print(
        f"Average Price : "
        f"{response.get('avgPrice')}"
    )

    print(
        f"Symbol        : "
        f"{response.get('symbol')}"
    )


def main():

    parser = argparse.ArgumentParser(
        description="Binance Futures Testnet Trading Bot"
    )

    parser.add_argument(
        "--symbol",
        required=True,
        help="BTCUSDT"
    )

    parser.add_argument(
        "--side",
        required=True,
        help="BUY or SELL"
    )

    parser.add_argument(
        "--type",
        required=True,
        help="MARKET or LIMIT"
    )

    parser.add_argument(
        "--quantity",
        required=True,
        type=float
    )

    parser.add_argument(
        "--price",
        type=float
    )

    args = parser.parse_args()

    try:

        symbol = validate_symbol(
            args.symbol
        )

        side = validate_side(
            args.side
        )

        order_type = validate_order_type(
            args.type
        )

        quantity = validate_quantity(
            args.quantity
        )

        print("\n===== ORDER REQUEST =====")

        print(f"Symbol   : {symbol}")
        print(f"Side     : {side}")
        print(f"Type     : {order_type}")
        print(f"Quantity : {quantity}")

        if order_type == "MARKET":

            response = place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            price = validate_price(
                args.price
            )

            print(f"Price    : {price}")

            response = place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print_response(response)

        print(
            "\nSUCCESS: Order placed successfully."
        )

    except Exception as e:

        logger.exception("CLI EXECUTION FAILED")

        print("\n===== ERROR =====")
        print(f"Reason : {e}")
        print("Status : FAILED")


if __name__ == "__main__":
    main()