import telebot
from colorama import *
init()
bot = telebot.TeleBot('7513792114:AAHBJSQQAABEHjbB9mupqvIDoKCRfZiq0Wg')
@bot.message_handler(commands=['start', 'help']) #отслеживание команды старт
def start(message):
    bot.reply_to(message, '❤️YOOOO MAAAN GODDAMN.❤️\n🤘Это бот для посылания нахуй, хуле.🤘\n🖕Введи имя того, кого хош послать🖕')
@bot.message_handler(func=lambda message: True)
def echo(message):
    print(Fore.GREEN + Style.BRIGHT +  + str('Имя: ' + message.from_user.first_name) + ', Фамилия: ' + str(message.from_user.last_name) + ', Юз: ' + str(message.from_user.username) + ', Соо: ' + message.text)
    bot.reply_to(message, message.text + ' пашел нахуй')
bot.polling(non_stop=True) #чтобы работало всегда