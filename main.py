#!/usr/bin/env python3
import os
import logging
import requests
import telebot
from telebot.apihelper import ApiTelegramException

# ✅ Logging setup
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)

# ✅ Load BOT_TOKEN securely
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN not found. Please set it in your environment.")

# ✅ Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# ✅ Clear existing webhook to avoid 409 error
def clear_webhook():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook"
    try:
        res = requests.get(url)
        if res.status_code == 200 and res.json().get("ok"):
            logging.info("✅ Webhook cleared successfully.")
        else:
            logging.warning(f"⚠️ Webhook not cleared: {res.text}")
    except requests.RequestException as e:
        logging.error(f"⚠️ Telegram API connection failed: {e}")

# ✅ /start command
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "👋 Welcome to Chat ID Bot!\nSend /id to get your Telegram chat ID.")

# ✅ /id command
@bot.message_handler(commands=['id'])
def handle_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"🆔 Your Chat ID: `{chat_id}`", parse_mode="Markdown")

# ✅ Start polling safely
def run_bot():
    clear_webhook()
    try:
        bot_info = bot.get_me()
        logging.info(f"🤖 Bot started as @{bot_info.username}")
        bot.polling(non_stop=True)
    except ApiTelegramException as e:
        if "Conflict" in str(e):
            logging.error("🚫 Bot conflict: another process is polling.")
        else:
            logging.error(f"❌ Telegram API error: {e}")
        raise  # optional: retry or exit

if __name__ == "__main__":
    run_bot()
