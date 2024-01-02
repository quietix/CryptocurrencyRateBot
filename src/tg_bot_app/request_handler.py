from src.tg_bot_app.modules.handler import Handler
from telebot import types


handler = Handler()


def handle_request(request_body):
    update = types.Update.de_json(request_body)
    handler.handle_request(update)