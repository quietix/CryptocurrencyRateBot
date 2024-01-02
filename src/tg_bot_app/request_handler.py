from src.apply_config_changes import bot
from telebot import types


class Handler:
    def handle_request(self, request_body):
        update = types.Update.de_json(request_body)
        bot.process_new_updates([update])
        chat_id = update.message.chat.id
        bot.reply_to(update.message, update.message.text)



handler = Handler()

def handle_request(request_body):
    handler.handle_request(request_body)
