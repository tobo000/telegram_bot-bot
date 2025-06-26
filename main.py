#!/usr/bin/env python
import os
import telebot
import logging

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

# ✅ Start polling
print("🤖 Bot is polling now...")
logging.info("Bot polling started...")
bot.polling()
