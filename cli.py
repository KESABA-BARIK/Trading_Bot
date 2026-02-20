import argparse
from bot.client import get_client
from bot.orders import place_order
from bot.validators import *
from bot.logging_config import setup_logging

def main():
    setup_logging()
    parser = argparse.ArgumentParser(description="Trading Bot")
    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price")
    args = parser.parse_args()

    try:
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.price, args.type)

        client = get_client()

        print("\nOrder Request Summary:")
        print(vars(args))

        order = place_order(
            client,
            args.symbol.upper(),
            args.side.upper(),
            args.type.upper(),
            args.quantity,
            args.price
        )

        print("\nOrder Response:")
        print(f"Order ID: {order.get('orderId')}")
        print(f"Status: {order.get('status')}")
        print(f"Executed Qty: {order.get('executedQty')}")
        print(f"Avg Price: {order.get('avgPrice')}")

        print("\nOrder placed successfully!")

    except Exception as e:
        print(f"\nOrder failed: {str(e)}")

if __name__ == "__main__":
    main()