import telebot
import webbrowser
from telebot import types

bot = telebot.TeleBot('6844479003:AAHJVyX0PIGk7zl1Ev6hKqMNA2IS6IQWvIA')


@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://ya.ru/')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Перейти на сайт 😀')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Удалить фото')
    btn3 = types.KeyboardButton('Изменить текст')
    markup.row(btn2, btn3)
    file = open('./Photo_hellow.jpeg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    #bot.send_audio(message.chat.id, file, reply_markup=markup)
    #bot.send_video(message.chat.id, file, reply_markup=markup)
    #bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'Перейти на сайт':
        bot.send_message(message.chat.id, 'Сайт открыт')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Фото удалено')



@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Перейти на сайт', url='https://ya.ru/')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Удалить фото', callback_data='delete')
    btn3 = types.InlineKeyboardButton('Изменить текст', callback_data='edit')
    markup.row(btn2, btn3)
    markup.add(types.InlineKeyboardButton('Teст', callback_data='edit'))
    bot.reply_to(message, 'Какое красивое фото!', reply_markup=markup)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edited_message_text('Edit text', callback.message.chat.id, callback.message.message_id)



@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')

@bot.message_handler()
def info(message):
    if message.text.lower() == 'Привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.polling(none_stop=True)

x=1