from src.apply_config_changes import bot
from telebot import types
from src.tg_bot_app.modules.response import Response


response = Response()


class Handler:
    @bot.message_handler(commands=['start', 'help'])
    def handle_request(self, update: types.Update):
        bot.process_new_updates([update])
        response.send_help_list(update)
