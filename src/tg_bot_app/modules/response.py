from src.apply_config_changes import bot
from telebot import types
from src.tg_bot_app import api_retriever


class Response:
    def send_message(self, chat_id, text):
        bot.send_message(chat_id, text)


    def send_help_list(self, message: types.Message):
        help_text = """🤖 Бот "Курс криптовалют" 🤖

Я допоможу вам:
1. Отримувати актуальні дані про курси обміну криптовалют
2. Рахувати ваші активи до та після проведення обміну валют

Для початку роботи з сервісом перейдіть у меню. Для цього скористайтеся командою /menu"""

        bot.reply_to(message, help_text)


    def ask_for_registration(self, message: types.Message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        reg_button = types.KeyboardButton(text="Поділитися телефоном", request_contact=True)

        markup.add(reg_button)

        bot.send_message(message.chat.id,
                        "Для того, щоб зареєструватися, потрібно поділитися своїм контактом",
                        reply_markup=markup)

    def send_menu(self, message: types.Message):
        markup = types.InlineKeyboardMarkup()
        markup.row_width = 3

        coins = api_retriever.json_r['data']['coins']
        for i in range(0, 9, 3):
            markup.add(types.InlineKeyboardButton(coins[i]['name'], callback_data=f"{coins[i]['name']}"),
                       types.InlineKeyboardButton(coins[i+1]['name'], callback_data=f"{coins[i+1]['name']}"),
                       types.InlineKeyboardButton(coins[i+2]['name'], callback_data=f"{coins[i+2]['name']}"))

        bot.send_message(message.chat.id, "Оберіть криптовалюту", reply_markup=markup)