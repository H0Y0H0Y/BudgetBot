import telebot
from datetime import datetime
from constants import BOT_TOKEN
from db.AccountCollection import AccountCollection
from db.TransactionCollection import TransactionCollection

bot = telebot.TeleBot(BOT_TOKEN)

# check if message.chat.id is in the account collection
def is_account_a_client(chat_id: int):
    account = AccountCollection()
    query = {"chat_id": chat_id}
    
    result = account.find_account(query)
    return result['chat_id'] == chat_id

@bot.message_handler(commands=['start'], func=lambda message: is_account_a_client(message.chat.id))
def send_welcome(message):
    bot.reply_to(message, "Hello there!")

@bot.message_handler(commands=['getChatId'])
def get_chat_id(message):
    bot.reply_to(message, message.chat.id)

# handle message with that can be a float or number
@bot.message_handler(
        func=lambda message: (message.text.isdigit() or message.text.replace('.', '', 1).isdigit())
        and is_account_a_client(message.chat.id)
)
def handle_number(message):
    transaction = TransactionCollection()
    
    utc_time = datetime.utcnow()
    
    record = {
        "chat_id": message.chat.id,
        "amount": float(message.text),
        "timestamp": utc_time
    }
    transaction.insert_transaction(record)
    bot.reply_to(message, "saving transaction...")

if __name__ == '__main__':
    bot.infinity_polling()