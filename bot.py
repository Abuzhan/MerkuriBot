import telebot
import config
import os
import utils
from telebot import types

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def starting_page(message):
    welcome_text = 'Добро пожаловать в онлайн-магазин Меркури! Воспользуйтесь нашим главным меню чтобы начать искать товары. Если вам нужна помощь введите команду /help.'
    f = open('images/logo.png', 'rb')
    values = ("Хиты продаж", "Популярные товары", "Популярные магазины", "Категории", "ЧАВО")
    markup = utils.generate_markup(values)
    bot.send_photo(message.chat.id, f, welcome_text, reply_markup=markup)



if __name__ == '__main__':
    bot.polling(none_stop=True)
    
