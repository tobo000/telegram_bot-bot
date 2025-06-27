import os
import telebot

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("No BOT_TOKEN provided.")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🟢 WELCOME TO CHAT ID BOT\n"
        "Send /id to get your Telegram ID\n"
        "Created by @bigboss_global_trade .")

@bot.message_handler(commands=['id'])
def chat_id(message):
    bot.reply_to(message, f"🆔 Your ID: {message.chat.id}", parse_mode="Markdown")

print("🤖 Bot is polling now...")
bot.polling(non_stop=True)
