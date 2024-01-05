import telebot.types

from src.apply_config_changes import bot
from telebot.types import Update, Message
from src.tg_bot_app.modules.response import Response
from src.tg_bot_app.modules.db_manager import DBManager
from src.tg_bot_app.states import MyStates


response = Response()
db_manager = DBManager()


@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    bot.set_state(user_id=message.from_user.id,
                  state=MyStates.register,
                  chat_id=message.chat.id)
    db_manager.add_user(message)
    response.send_help_list(message)


@bot.message_handler(state="*", commands=['help'])
def help(message: telebot.types.Message):
    response.send_help_list(message)


@bot.message_handler(state=MyStates.register, commands=['register'])
def register(message: telebot.types.Message):
    response.ask_for_registration(message)


@bot.message_handler(state=MyStates.register, content_types=['contact'])
def contact_handler(message: Message):
    phone_number = message.contact.phone_number

    if db_manager.account_exists(phone_number):
       bot.send_message(message.chat.id, "Ви вже зареєстровані.\nДля того, щоб перейти до головного меню, натисність /menu",
                        reply_markup=telebot.types.ReplyKeyboardRemove())
    else:
        db_manager.add_account(message.from_user.id, phone_number)
        bot.send_message(message.chat.id, "Реєстрацію пройдено успішно!\nДля того, щоб перейти до головного меню натисність /menu",
                     reply_markup=telebot.types.ReplyKeyboardRemove())
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(commands=['menu'])
def menu(message: telebot.types.Message):
    if db_manager.is_registered(message.from_user.id):
        response.send_menu(message)
        bot.set_state(message.from_user.id, MyStates.menu, message.chat.id)
    else:
        bot.send_message(message.chat.id, "Для того, щоб перейти до головного меню, потрібно пройти реєстрацію.\n\nЗареєструватися можна за допомогою команди /register")
        bot.set_state(message.from_user.id, MyStates.register, message.chat.id)


