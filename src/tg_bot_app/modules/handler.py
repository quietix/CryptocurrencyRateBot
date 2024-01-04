from src.apply_config_changes import bot
from telebot import types
from src.tg_bot_app.modules.response import Response
from src.tg_bot_app.modules.db_managers.db_manager_proxy import DBManagerProxy
from django.apps import apps


response = Response()
db_manager = DBManagerProxy()


class Handler:
    @bot.message_handler(commands=['start'])
    def handle_request(self, update: types.Update):
        bot.process_new_updates([update])
        users = apps.get_model('tg_bot_app', 'User').objects.all()
        for user in users:
            response.send_message(update.message.chat.id, user)