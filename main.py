import keys
import telebot
import values
import db_connect

bot = telebot.TeleBot(keys.BOT_TOKEN)
db = db_connect.Database()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_id = message.from_user.id
    # username = message.from_user.
    if db.user_exists(user_id):
        bot.send_message(user_id, 'Hi!')
    else:
        # db.add_user(user_id)
        bot.send_message(message.from_user.id, values.start_message)


if __name__ == '__main__':
    bot.infinity_polling()