from telebot import TeleBot
import dotenv

dotenv.load_dotenv()

token = dotenv.dotenv_values('.env')['TOKEN']
url = dotenv.dotenv_values('.env')['URL']

bot = TeleBot(token)
bot.set_webhook(url)