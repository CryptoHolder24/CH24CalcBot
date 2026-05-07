<<<<<<< HEAD
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден. Проверь .env файл")
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Соответствие тикеров CoinGecko ID
COINS = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "USDT": "tether",
    "BNB": "binancecoin",
    "SOL": "solana",
    "XRP": "ripple",
    "ADA": "cardano",
    "DOGE": "dogecoin",
    "TON": "the-open-network"
}

# Получение курса
def get_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    data = requests.get(url).json()
    return data.get(coin_id, {}).get("usd", None)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я крипто-калькулятор канала CryptoHolder24\n"
        "Я всегда знаю актуальные курсы криптовалют и могу подсказать их тебе\n\n"
        "Введи, например:\n"
        "BTC\n"
        "0.5 BTC\n"
        "1000 USDT"
    )

# Обработка сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.upper().split()

    try:
        if len(text) == 1:
            symbol = text[0]

            if symbol not in COINS:
                await update.message.reply_text("Не знаю такую монету 😕")
                return

            coin_id = COINS[symbol]
            price = get_price(coin_id)

            if price:
                await update.message.reply_text(f"{symbol} = ${price}")
            else:
                await update.message.reply_text("Ошибка получения курса")

        elif len(text) == 2:
            amount = float(text[0])
            symbol = text[1]

            if symbol not in COINS:
                await update.message.reply_text("Не знаю такую монету 😕")
                return

            coin_id = COINS[symbol]
            price = get_price(coin_id)

            if price:
                result = amount * price
                await update.message.reply_text(f"{amount} {symbol} = ${round(result, 2)}")
            else:
                await update.message.reply_text("Ошибка получения курса")

    except:
        await update.message.reply_text("Ошибка. Пример: 0.1 BTC")

# Запуск
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
=======
import requests
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
if not TOKEN:
    raise ValueError("❌ BOT_TOKEN не найден. Проверь .env файл")
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Соответствие тикеров CoinGecko ID
COINS = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "USDT": "tether",
    "BNB": "binancecoin",
    "SOL": "solana",
    "XRP": "ripple",
    "ADA": "cardano",
    "DOGE": "dogecoin",
    "TON": "the-open-network"
}

# Получение курса
def get_price(coin_id):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    data = requests.get(url).json()
    return data.get(coin_id, {}).get("usd", None)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Я крипто-калькулятор канала CryptoHolder24\n"
        "Я всегда знаю актуальные курсы криптовалют и могу подсказать их тебе\n\n"
        "Введи, например:\n"
        "BTC\n"
        "0.5 BTC\n"
        "1000 USDT"
    )

# Обработка сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.upper().split()

    try:
        if len(text) == 1:
            symbol = text[0]

            if symbol not in COINS:
                await update.message.reply_text("Не знаю такую монету 😕")
                return

            coin_id = COINS[symbol]
            price = get_price(coin_id)

            if price:
                await update.message.reply_text(f"{symbol} = ${price}")
            else:
                await update.message.reply_text("Ошибка получения курса")

        elif len(text) == 2:
            amount = float(text[0])
            symbol = text[1]

            if symbol not in COINS:
                await update.message.reply_text("Не знаю такую монету 😕")
                return

            coin_id = COINS[symbol]
            price = get_price(coin_id)

            if price:
                result = amount * price
                await update.message.reply_text(f"{amount} {symbol} = ${round(result, 2)}")
            else:
                await update.message.reply_text("Ошибка получения курса")

    except:
        await update.message.reply_text("Ошибка. Пример: 0.1 BTC")

# Запуск
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
>>>>>>> 11c8523 (secure bot)
