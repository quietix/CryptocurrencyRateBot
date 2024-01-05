from telebot.handler_backends import State, StatesGroup #States

class MyStates(StatesGroup):
    register = State()
    menu = State()