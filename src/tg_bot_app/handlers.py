import telebot.types

from src.apply_config_changes import bot
from telebot.types import Update, Message
from src.tg_bot_app.modules.response import Response
from src.tg_bot_app.modules.db_manager import DBManager


response = Response()
db_manager = DBManager()


@bot.message_handler(commands=['help'])
def help(message: telebot.types.Message):
    response.send_help_list(message)


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    db_manager.add_user(message)
    response.send_help_list(message)


@bot.message_handler(commands=['register'])
def register(message: telebot.types.Message):
    response.ask_for_registration(message)


@bot.message_handler(content_types=['contact'])
def contact_handler(message: Message):
    phone_number = message.contact.phone_number

    if db_manager.account_exists(phone_number):
       bot.send_message(message.chat.id, "Ви вже зареєстровані.\nДля того, щоб перейти до головного меню/ натисність /menu",
                        reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        db_manager.add_account(message.from_user.id, phone_number)
        bot.send_message(message.chat.id, "Реєстрацію пройдено успішно!\nДля того, щоб перейти до головного меню/ натисність /menu",
                     reply_markup=telebot.types.ReplyKeyboardRemove())
