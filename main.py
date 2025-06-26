#!/usr/bin/env python
import os
import telebot
import logging
import time
from telebot.apihelper import ApiTelegramException

# ✅ Enable logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# ✅ Get token from environment variable
bot_token = os.environ.get("BOT_TOKEN")
if not bot_token:
    raise ValueError("No BOT_TOKEN found. Make sure it's set in Render environment variables.")

bot = telebot.TeleBot(bot_token)

# ✅ /start handler
@bot.message_handler(commands=['start'])
def wlcm_msg(message):
    wlcm_text = """  WELCOME TO CHAT ID BOT 
Send /id command to Get your Id
created by @bigboss_global_trade"""
    bot.reply_to(message, wlcm_text)

# ✅ /id handler
@bot.message_handler(commands=['id'])
def send_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"Your Id: {chat_id}")

# ✅ Polling loop with retry to prevent crash from 409
def run_bot():
    try:
        print("🤖 Bot is polling now...")
        logging.info(f"Connected as: {bot.get_me().username}")
        bot.polling(non_stop=True)
    except ApiTelegramException as e:
        if "Conflict" in str(e):
            logging.error("🚨 Another instance is running. Run /deleteWebhook to clear webhook if needed.")
        else:
            logging.error(f"❌ Telegram API error: {e}")
        time.sleep(10)
        run_bot()  # retry

if __name__ == "__main__":
    run_bot()
