from bot.logging_config import setup_logger

logger = setup_logger()

def place_order(client, symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"REQUEST | {symbol} {side} {order_type} {quantity} {price}")

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)

        logger.info(f"RESPONSE | {response}")
        return response

    except Exception as e:
        logger.error(f"ERROR | {str(e)}")
        raise