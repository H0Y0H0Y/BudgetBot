import telebot
from constants import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello there!")

if __name__ == '__main__':
    bot.infinity_polling()