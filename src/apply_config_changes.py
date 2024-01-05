from telebot import TeleBot
import dotenv
from telebot.storage import StateMemoryStorage
from telebot import custom_filters


dotenv.load_dotenv()

token = dotenv.dotenv_values('.env')['TOKEN']
url = dotenv.dotenv_values('.env')['URL']

state_storage = StateMemoryStorage()

bot = TeleBot(token, threaded=False, state_storage=state_storage)
bot.set_webhook(url)
bot.add_custom_filter(custom_filters.StateFilter(bot))
