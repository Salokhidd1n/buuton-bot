import datetime
import telebot
import gtts
import os
from telebot import  types

current_path = os.path.abspath(os.getcwd())

token = "2080506950:AAFGvpV-1F_jpkGq6x9LCBSPsq7h_SjlGDs"

my_bot = telebot.TeleBot(token)
@my_bot.message_handler(commands=["start", "старт"])
def say_hello(message):
    my_bot.send_message(message.chat.id, "XOJ")

@my_bot.message_handler(commands=['xoj'])
def xoj(message):
    markup = types.ReplyKeyboardMarkup()
    buutonA = types.KeyboardButton('A')
    buutonB = types.KeyboardButton('B')
    buutonC = types.KeyboardButton('C')
    buutonD = types.KeyboardButton('D')
    buutonL = types.KeyboardButton('L')
    buutonO = types.KeyboardButton('O')
    buutonR = types.KeyboardButton('R')
    buutonF = types.KeyboardButton('F')
    buutonE = types.KeyboardButton('E')
    buutonY = types.KeyboardButton('Y')
    buutonJ = types.KeyboardButton('J')
    buutonG = types.KeyboardButton('G')
    buutonH = types.KeyboardButton('H')
    buutonV = types.KeyboardButton('V')
    markup.row(buutonA,buutonB,buutonC,buutonV,buutonJ,buutonG, buutonL,buutonO,buutonR,buutonE,buutonY,buutonF,buutonH)
    markup.row(buutonD)
    my_bot.send_message(message.chat.id,'working', reply_markup=markup)




@my_bot.message_handler(commands=['apple'])
def apple(message):
    markup = types.InlineKeyboardMarkup()
    buutonA = types.InlineKeyboardButton('A', callback_data="a")
    buutonB = types.InlineKeyboardButton('B', callback_data="b")
    buutonC = types.InlineKeyboardButton('C', callback_data="c")
    buutonD = types.InlineKeyboardButton('D', callback_data="d")

    markup.row(buutonA,buutonB,buutonC)
    markup.row(buutonD)
    my_bot.send_message(message.chat.id,'working', reply_markup=markup)



@my_bot.message_handler(content_types=["text"])
def say_any(message):
    say = gtts.gTTS(message.text, lang="ru")
    file_name = datetime.datetime.today()
    say.save(f"{file_name}.mp3")
    final_path = f'{current_path}/{file_name}.mp3'
    audio_file = open(final_path, 'rb')
    my_bot.send_message(message.chat.id, "XOJ RABOTAYT")
    my_bot.send_audio(message.chat.id, audio_file)


print("XOJ RABOTAYT")
my_bot.infinity_polling()