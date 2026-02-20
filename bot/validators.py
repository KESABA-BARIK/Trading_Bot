def validate_side(side):
    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

def validate_order_type(order_type):
    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

def validate_quantity(quantity):
    if float(quantity) <= 0:
        raise ValueError("Quantity must be positive")

def validate_price(price, order_type):
    if order_type.upper() == "LIMIT" and (price is None or float(price) <= 0):
        raise ValueError("Price required for LIMIT order and must be positive")