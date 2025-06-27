import os
import logging
import requests
import telebot

# Logging
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not set!")

bot = telebot.TeleBot(BOT_TOKEN)

# Clear webhook
def clear_webhook():
    res = requests.get(f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook")
    if res.ok:
        logging.info("✅ Webhook cleared")
    else:
        logging.error(f"Failed to clear webhook: {res.text}")

# Commands
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "🤖 Welcome! Send /id to get your ID")

@bot.message_handler(commands=['id'])
def handle_id(message):
    bot.reply_to(message, f"🆔 Your ID: `{message.chat.id}`", parse_mode="Markdown")

# Start bot
if __name__ == "__main__":
    clear_webhook()
    logging.info("🤖 Bot starting...")
    bot.polling(non_stop=True)
