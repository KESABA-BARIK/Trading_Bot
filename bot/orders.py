import logging

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        if order_type == 'MARKET':
            logging.info(f"Placing MARKET order | {symbol} | {side} | Qty={quantity}")
        else:
            logging.info(f"Placing MARKET order | {symbol} | {side} | Qty={quantity} | Price={price}")

        if order_type == "MARKET":
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity
            )
            order_status = client.futures_get_order(
                symbol=symbol,
                orderId=order['orderId']
            )
        else:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type=order_type,
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            order_status = client.futures_get_order(
                symbol=symbol,
                orderId=order['orderId']
            )

        logging.info(f"Order Executed | "
            f"ID={order.get('orderId')} | "
            f"Symbol={order.get('symbol')} | "
            f"Side={order.get('side')} | "
            f"Type={order.get('type')} | "
            f"Status={order.get('status')} | "
            f"ExecutedQty={order.get('executedQty')} | "
            f"AvgPrice={order.get('avgPrice')}"
                     )
        return order_status

    except Exception as e:
        logging.error(
            f"Order Failed | "
            f"Symbol={symbol} | "
            f"Side={side} | "
            f"Type={order_type} | "
            f"Error={str(e)}"
        )
        raise