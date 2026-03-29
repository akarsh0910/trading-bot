def validate_symbol(symbol: str) -> str:
    symbol = symbol.strip().upper()
    if not symbol.endswith("USDT"):
        raise ValueError("Symbol must end with USDT (e.g., BTCUSDT)")
    return symbol

def validate_side(side: str) -> str:
    side = side.strip().upper()
    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")
    return side

def validate_order_type(order_type: str) -> str:
    order_type = order_type.strip().upper()
    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")
    return order_type

def validate_quantity(quantity: str) -> float:
    quantity = float(quantity)
    if quantity <= 0:
        raise ValueError("Quantity must be > 0")
    return quantity

def validate_price(price: str) -> float:
    price = float(price)
    if price <= 0:
        raise ValueError("Price must be > 0")
    return price