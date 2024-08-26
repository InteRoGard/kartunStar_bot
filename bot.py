import telebot

token = "7433544490:AAHNGYqJfVRZQUpRs_QTvERyYIaTqwhfO3Q"
# telebot.apihelper.proxy = {''}
bot = telebot.TeleBot(token = token)

@bot.message_handler(content_types=['text'])

def echo(message):
    text = message.text
    user = message.chat.id
    bot.send_message(user, text)

bot.polling(non_stop = True)