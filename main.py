#!/usr/bin/env python
import os
import time
import logging
import requests
import telebot
from telebot.apihelper import ApiTelegramException

# ✅ Logging setup
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ✅ Load bot token
BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN not found. Set it in Render environment variables.")

# ✅ Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# ✅ /start command
@bot.message_handler(commands=['start'])
def start_command(message):
    welcome_text = """🟢 WELCOME TO CHAT ID BOT\nSend /id to get your Telegram ID\nCreated by @bigboss_global_trade"""
    bot.reply_to(message, welcome_text)

# ✅ /id command
@bot.message_handler(commands=['id'])
def id_command(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"🆔 Your Chat ID: `{chat_id}`", parse_mode="Markdown")

# ✅ Clear any existing webhook to avoid 409 conflict
def clear_webhook():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200 and res.json().get("ok"):
            logging.info("✅ Telegram webhook cleared successfully.")
        else:
            logging.warning(f"⚠️ Failed to clear webhook: {res.text}")
    except requests.RequestException as err:
        logging.warning(f"⚠️ Could not connect to Telegram API: {err}")

# ✅ Run bot with retry on 409 or connection errors
def run_bot():
    clear_webhook()
    try:
        me = bot.get_me()
        logging.info(f"🤖 Bot connected as @{me.username}")
        print("🤖 Bot is now polling...")
        bot.polling(non_stop=True)
    except ApiTelegramException as e:
        if "Conflict" in str(e):
            logging.error("🚫 Conflict error: another polling session is running. Retry later or kill the other instance.")
        else:
            logging.error(f"❌ Telegram API error: {e}")
        time.sleep(10)
        run_bot()  # Optional retry loop

if __name__ == "__main__":
    run_bot()
