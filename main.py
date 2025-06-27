import os
import telebot
import requests
import logging

# Logging
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = os.environ.get("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN not found!")

bot = telebot.TeleBot(BOT_TOKEN)

# Clear webhook
def clear_webhook():
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook"
    try:
        r = requests.get(url)
        if r.ok:
            logging.info("✅ Webhook cleared.")
        else:
            logging.warning(f"⚠️ Failed to clear webhook: {r.text}")
    except Exception as e:
        logging.error(f"⚠️ Error clearing webhook: {e}")

# Commands
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 Welcome! Send /id to get your chat ID.")

@bot.message_handler(commands=['id'])
def chat_id(message):
    bot.reply_to(message, f"🆔 Your chat ID: `{message.chat.id}`", parse_mode="Markdown")

# Run bot
if __name__ == "__main__":
    clear_webhook()
    logging.info("🤖 Bot polling...")
    bot.polling(non_stop=True)
