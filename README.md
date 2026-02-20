# Binance Futures Testnet Trading Bot

A lightweight Python CLI trading bot for placing **Market** and **Limit** orders on [Binance Futures Testnet (USDT-M)](https://testnet.binancefuture.com). Built with clean separation between the API client layer and CLI layer, structured logging, and robust input validation.

---

## Project Structure

```
trading_bot/
├── bot/
│   ├── __init__.py
│   ├── client.py           # Binance client wrapper
│   ├── orders.py           # Order placement logic
│   ├── validators.py       # Input validation
│   └── logging_config.py   # Logging setup
├── cli.py                  # CLI entry point
├── trading_bot.log         # Auto-generated log file
├── .env                    # API credentials (not committed)
├── README.md
└── requirements.txt
```

---

## Setup

### 1. Get Testnet API Credentials

1. Go to [https://testnet.binancefuture.com](https://testnet.binancefuture.com) and log in with your GitHub account.
2. Navigate to **API Key** section and generate a key pair.
3. Copy your **API Key** and **Secret Key**.

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/trading-bot.git
cd trading-bot
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
BINANCE_KEY=your_testnet_api_key
BINANCE_SECRET=your_testnet_api_secret
```

> ⚠️ Never commit your `.env` file. Add it to `.gitignore`.

---

## How to Run

The bot is run via `cli.py` with the following arguments:

| Argument     | Required          | Description                        |
|--------------|-------------------|------------------------------------|
| `--symbol`   | Yes               | Trading pair (e.g., `BTCUSDT`)     |
| `--side`     | Yes               | `BUY` or `SELL`                    |
| `--type`     | Yes               | `MARKET` or `LIMIT`                |
| `--quantity` | Yes               | Quantity to trade (must be > 0)    |
| `--price`    | LIMIT orders only | Limit price (must be > 0)          |

### Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01
```

### Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.01 --price 85000
```

### Example Output

```
Order Request Summary:
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': '0.01', 'price': None}

Order Response:
Order ID: 3426139
Status: FILLED
Executed Qty: 0.01
Avg Price: 84231.50

Order placed successfully!
```

---

## Logging

All API requests, responses, and errors are automatically logged to `trading_bot.log` in the project root.

**Log format:**
```
YYYY-MM-DD HH:MM:SS | LEVEL | Message
```

**Example log entries:**
```
2025-07-10 14:22:01 | INFO | Placing MARKET order | BTCUSDT | BUY | Qty=0.01
2025-07-10 14:22:02 | INFO | Order Executed | ID=3426139 | Symbol=BTCUSDT | Side=BUY | Type=MARKET | Status=FILLED | ExecutedQty=0.01 | AvgPrice=84231.5
2025-07-10 14:25:10 | INFO | Placing LIMIT order | BTCUSDT | SELL | Qty=0.01 | Price=85000
2025-07-10 14:25:11 | INFO | Order Executed | ID=3426201 | Symbol=BTCUSDT | Side=SELL | Type=LIMIT | Status=NEW | ExecutedQty=0.0 | AvgPrice=0
```

---

## Error Handling

The bot validates all inputs before hitting the API and surfaces clear error messages:

```bash
# Invalid side
python cli.py --symbol BTCUSDT --side HOLD --type MARKET --quantity 0.01
# → Order failed: Side must be BUY or SELL

# Missing price for LIMIT order
python cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01
# → Order failed: Price required for LIMIT order and must be positive

# Negative quantity
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity -1
# → Order failed: Quantity must be positive
```

API errors and network failures are also caught and logged with full context.

---

## Assumptions

- All orders are placed on **Binance Futures Testnet (USDT-M)** only — not live/mainnet.
- Limit orders use `timeInForce=GTC` (Good Till Cancelled) by default.
- The bot does not manage open positions or cancel existing orders — it is order-placement only.
- Symbol input is case-insensitive and normalized to uppercase automatically.
- Minimum quantity and price precision requirements depend on the symbol's exchange rules on testnet; invalid values will return an API error.

---

## Requirements

See `requirements.txt`:

```
python-binance
python-dotenv
```

Install with:

```bash
pip install -r requirements.txt
```

---
