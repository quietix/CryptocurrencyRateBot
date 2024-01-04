from src.tg_bot_app.modules.db_managers.db_manager import DBManager
from telebot.types import Update


class DBManagerProxy(DBManager):
    _db_manager = DBManager()

    def add_user(self, update: Update):
        self._db_manager.add_user(update)

    def check_user_data(self, update: Update):
        # user_id = update.message.from_user.id
        # records_number = Users.
        # print(Users)
        pass
# user = Users.
