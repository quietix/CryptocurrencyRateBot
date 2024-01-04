from src.apply_config_changes import bot
from telebot import types


class Response:
    def send_message(self, chat_id, text):
        bot.send_message(chat_id, text)


    def send_help_list(self, message: types.Message):
        help_text = """🤖 Бот "Курс криптовалют" 🤖

Я допоможу вам:
1. Отримувати актуальні дані про курси обміну криптовалют
2. Рахувати ваші активи до та після проведення обміну валют"""

        bot.reply_to(message, help_text)


    def ask_for_registration(self, message: types.Message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        reg_button = types.KeyboardButton(text="Поділитися телефоном", request_contact=True)

        markup.add(reg_button)

        bot.send_message(message.chat.id,
                        "Для того, щоб зареєструватися, потрібно поділитися своїм контактом",
                        reply_markup=markup)