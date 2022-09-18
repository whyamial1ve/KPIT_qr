import keys
import telebot
import messages

bot = telebot.TeleBot(keys.BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.from_user.id, messages.start_message)


if __name__ == '__main__':
    bot.infinity_polling()