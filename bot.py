import telebot
from constants import BOT_TOKEN
from db.AccountCollection import AccountCollection

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: is_account_a_client(message.chat.id))
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Hello there!")

@bot.message_handler(commands=['getChatId'])
def get_chat_id(message):
    bot.reply_to(message, message.chat.id)

# handle message with that can be a float or number
@bot.message_handler(func=lambda message: is_account_a_client(message.chat.id))
@bot.message_handler(func=lambda message: message.text.isdigit() or message.text.replace('.', '', 1).isdigit())
def handle_number(message):
    bot.reply_to(message, "You sent a number")

# check if message.chat.id is in the account collection
def is_account_a_client(chat_id):
    account = AccountCollection()
    query = {"chat_id": chat_id}
    
    result = account.find_record(query)
    return result['chat_id'] == chat_id

if __name__ == '__main__':
    bot.infinity_polling()