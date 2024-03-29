import requests
import dotenv
from src.apply_config_changes import bot
from telebot import types


headers = {
  'x-access-token': dotenv.dotenv_values('.env')['API_CRYPTO']
}

response = requests.request("GET", "https://api.coinranking.com/v2/coins", headers=headers)

json_r = response.json()

coins = json_r['data']['coins']

# for coin in coins:
#   print(f"price in dollars = {coin['price']}")
#   print(f"price in btc = {coin['btcPrice']}")
#
