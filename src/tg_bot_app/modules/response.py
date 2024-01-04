from src.apply_config_changes import bot
from telebot import types


class Response:
    def send_message(self, chat_id, text):
        bot.send_message(chat_id, text)


    def send_help_list(self, update: types.Update):
        help_text = """🤖 Бот "Курс криптовалют" 🤖

Я допоможу вам:
1. Отримувати актуальні дані про курси обміну криптовалют
2. Рахувати ваші активи до та після проведення обміну валют"""

        bot.reply_to(update.message, help_text)

