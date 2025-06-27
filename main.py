import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN provided.")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "👋 Welcome to the bot! Send /id to get your ID.")

@bot.message_handler(commands=['id'])
def send_id(message):
    bot.reply_to(message, f"🆔 Your ID: {message.chat.id}, parse_mode="Markdown")

print("🤖 Bot is polling now...")
bot.polling(non_stop=True)
