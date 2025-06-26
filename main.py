#!/usr/bin/env python
import os
import telebot
import logging
import time
import requests
from telebot.apihelper import ApiTelegramException

# ✅ Enable logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ✅ Load token from environment
bot_token = os.environ.get("BOT_TOKEN")
if not bot_token:
    raise ValueError("No BOT_TOKEN found. Make sure it's set in Render environment variables.")

bot = telebot.TeleBot(bot_token)

# ✅ /start command
@bot.message_handler(commands=['start'])
def wlcm_msg(message):
    wlcm_text = """  WELCOME TO CHAT ID BOT 
Send /id command to Get your Id
created by @bigboss_global_trade"""
    bot.reply_to(message, wlcm_text)

# ✅ /id command
@bot.message_handler(commands=['id'])
def send_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"Your Id: {chat_id}")

# ✅ Clear any existing webhook automatically
def clear_webhook():
    url = f"https://api.telegram.org/bot{bot_token}/deleteWebhook"
    try:
        res = requests.get(url, timeout=5)
        if res.status_code == 200 and res.json().get("ok"):
            logging.info("✅ Webhook cleared successfully.")
        else:
            logging.warning(f"⚠️ Failed to clear webhook: {res.text}")
    except requests.RequestException as e:
        logging.warning(f"⚠️ Webhook check failed: {e}")

# ✅ Start polling with retry
def run_bot():
    clear_webhook()  # clear any conflicting webhook
    try:
        logging.info("Connecting to Telegram...")
        me = bot.get_me()
        logging.info(f"🤖 Connected as @{me.username}")
        print("🤖 Bot is polling now...")
        bot.polling(non_stop=True)
    except ApiTelegramException as e:
        if "Conflict" in str(e):
            logging.error("🚨 Conflict detected: another instance is polling. Stopping.")
        else:
            logging.error(f"❌ API Exception: {e}")
        time.sleep(10)
        run_bot()  # Retry loop

if __name__ == "__main__":
    run_bot()
