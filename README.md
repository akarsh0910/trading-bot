# Binance Futures Testnet Trading Bot

A simple Python CLI trading bot that places *MARKET* and *LIMIT* orders on *Binance Futures Testnet (USDT-M)*.  
The project follows a clean modular structure with validation, logging, and error handling.


## Features

- Supports *BUY* and *SELL*
- Supports *MARKET* and *LIMIT* orders
- CLI-based user input
- Input validation
- Logging of API requests, responses, and errors



## Project Structure

```text
TRADING_BOT/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   └── trading_bot.log
│
├── cli.py
├── .env
├── .gitignore
├── README.md
└── requirements.txt

## Requirements 

- Python 3.x installed
- Internet connection
- Binance Futures Testnet API Key & Secret

## How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
2. In .env file,Add your API keys
Run the program: python cli.py


---

##  Example Input 

BTCUSDT  
BUY  
MARKET  
0.002  

OR  

BTCUSDT  
SELL  
LIMIT  
0.002  
65000
