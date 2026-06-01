# Binance Futures Testnet Trading Bot

A simplified Python-based trading bot that places **Market** and **Limit** orders on the **Binance Futures Testnet (USDT-M)** using a command-line interface (CLI).

This project demonstrates API integration, structured Python development, input validation, logging, and exception handling.

---

## Features

* Place **Market Orders**
* Place **Limit Orders**
* Support for **BUY** and **SELL**
* Command-line interface using `argparse`
* Input validation
* Logging of API requests, responses, and errors
* Exception handling
* Binance Futures Testnet integration

---

## Project Structure

```
trading_bot/
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
├── requirements.txt
├── README.md
├── .env.example
└── .gitignore
```

---

## Technologies Used

* Python 3.x
* python-binance
* python-dotenv
* Binance Futures Testnet API

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/jayant-abhinav/trading_bot.git

cd trading_bot
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Configure API Credentials

Create a `.env` file in the project root:

```
BINANCE_API_KEY=YOUR_API_KEY
BINANCE_API_SECRET=YOUR_SECRET_KEY
```

**Base URL used:**

```
https://testnet.binancefuture.com
```

Instead of uploading `.env`, a `.env.example` file is included as a reference for required environment variables.


---

## How to Run

### Market Buy Order

```
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Market Sell Order

```
python cli.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Limit Buy Order

```
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.005 --price 50000
```

### Limit Sell Order

```
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.005 --price 120000
```

---

## CLI Parameters

| Parameter    | Description               | Example   |
| ------------ | ------------------------- | --------- |
| `--symbol`   | Trading symbol            | `BTCUSDT` |
| `--side`     | BUY or SELL               | `BUY`     |
| `--type`     | MARKET or LIMIT           | `MARKET`  |
| `--quantity` | Order quantity            | `0.001`   |
| `--price`    | Required for LIMIT orders | `50000`   |

---

## Example Output

### Market Order

```
===== ORDER RESPONSE =====
Order ID      : 13678286908
Status        : FILLED
Executed Qty  : 0.0010
Average Price : 72832.300000
Symbol        : BTCUSDT
```

### Limit Order

```
===== ORDER RESPONSE =====
Order ID      : 13679116587
Status        : NEW
Executed Qty  : 0.0000
Average Price : 0.00
Symbol        : BTCUSDT
```

---

## Logging

All API requests, responses, and errors are logged in:

```text
logs/trading_bot.log
```

The log file contains records for:

* Market orders
* Limit orders
* API responses
* Error logs


---

## Error Handling

The application handles:

* Invalid order side
* Invalid order type
* Missing LIMIT order price
* Invalid quantity
* Binance API errors
* Timestamp synchronization issues
* Network/API failures

---

## Assumptions

* Binance Futures Testnet account is already configured.
* Valid API credentials are available.
* User has virtual testnet funds.
* Only **USDT futures pairs** are supported.
* Market orders return **FILLED** immediately.
* Limit orders may remain **NEW** until the target price is reached.

---

