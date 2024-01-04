from telebot.types import Update
from abc import ABC, abstractmethod


class DBManager(ABC):
    def add_user(self, update: Update):
        user = update.message.from_user
        user_to_add = Users(UserID=user.id,
              Name=user.first_name,
              Surname=user.last_name,
              Username=user.username)
        user_to_add.save()


    def delete_user(self):
        pass

    def get_user(self):
        '''
        Returns information about user in json
        '''
        pass