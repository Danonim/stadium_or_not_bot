import config
import telebot
from telebot import  types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Я на стадіоні?")
    markup.add(button)

    bot.send_message(message.chat.id, "Доброго ранку!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def stadium_or_not(message):

    answer = "Я не знаю😅"

    if message.text == "Я на стадіоні?":
        bot.send_message(message.chat.id, answer)
    else:
        bot.send_message(message.chat.id, "Ти шо кнопку не бачиш?🤨")

bot.infinity_polling()
