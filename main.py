#!/usr/bin/env python

import telebot
from keep_alive import keep_alive

keep_alive()

bot_token = "7349804202:AAEWcMMSPQCO-YLA7gcgMK3kQ-ZVzt8nsuo" # add your telegram bot token

bot = telebot.TeleBot(bot_token)

@bot.message_handler(commands=['start'])

def wlcm_msg(message):
    wlcm_text = """  WELLCOME TO CHAT ID BOT 
    Send /id command to Get your Id
created by @bigboss_global_trade""" # add your username 
    bot.reply_to(message, wlcm_text)

@bot.message_handler(commands=['id'])
def send_id(message):
    chat_id = message.chat.id 
    bot.reply_to(message, f"Your Id: {chat_id}")
bot.polling()
