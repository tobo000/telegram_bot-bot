#!/usr/bin/env python

#!/usr/bin/env python

import os
import telebot
from keep_alive import keep_alive

keep_alive()

# Get bot token from environment variable
bot_token = os.environ.get("7288959855:AAGVVGAxeTrYzQMbsb-h__8CGTi2SJjVpe4")
if not bot_token:
    raise ValueError("No BOT_TOKEN found. Make sure it's set in Render environment variables.")

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])
def wlcm_msg(message):
    wlcm_text = """  WELCOME TO CHAT ID BOT 
    Send /id command to Get your Id
created by @bigboss_global_trade"""
    bot.reply_to(message, wlcm_text)

@bot.message_handler(commands=['id'])
def send_id(message):
    chat_id = message.chat.id
    bot.reply_to(message, f"Your Id: {chat_id}")

bot.polling()
