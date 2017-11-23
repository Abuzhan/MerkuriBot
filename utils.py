from telebot import types

def generate_markup(values):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    for item in values:
        markup.add(item)
    return markup
