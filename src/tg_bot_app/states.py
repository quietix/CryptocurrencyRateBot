from telebot.handler_backends import State, StatesGroup

class MyStates(StatesGroup):
    register = State()
    menu = State()
