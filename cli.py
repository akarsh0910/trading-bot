from bot.client import get_binance_client
from bot.orders import place_order
from bot.validators import *

def main():
    try:
        print("=== Binance Futures Testnet Bot ===")

        symbol = validate_symbol(input("Symbol (BTCUSDT): "))
        side = validate_side(input("Side (BUY/SELL): "))
        order_type = validate_order_type(input("Order Type (MARKET/LIMIT): "))
        quantity = validate_quantity(input("Quantity: "))

        price = None
        if order_type == "LIMIT":
            price = validate_price(input("Price: "))

        print("\n--- Summary ---")
        print(symbol, side, order_type, quantity, price)

        client = get_binance_client()
        response = place_order(client, symbol, side, order_type, quantity, price)

        print("\n--- Response ---")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()