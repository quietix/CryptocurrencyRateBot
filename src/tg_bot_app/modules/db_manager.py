from telebot.types import Message
from django.apps import apps
from .response import Response


class DBManager():
    response = Response()

    def add_user(self, message: Message):
        users_model = apps.get_model('tg_bot_app', 'User')
        new_user = users_model(message.from_user.id,
                         message.from_user.first_name,
                         message.from_user.last_name,
                         message.from_user.username)
        new_user.save()


    def delete_user(self, message: Message):
        users_model = apps.get_model('tg_bot_app', 'User')
        user_to_delete = users_model.objects.get(pk=message.from_user.id)
        user_to_delete.delete()


    def account_exists(self, phone_number) -> bool:
        '''
        Check if account exists
        '''
        accounts = apps.get_model('tg_bot_app', 'Account').objects.all()

        for account in accounts:
            if phone_number == account.phone:
                return True

        return False


    def add_account(self, user_id, phone):
        accounts_model = apps.get_model('tg_bot_app', 'Account')
        users_model = apps.get_model('tg_bot_app', 'User')

        user = users_model.objects.get(user_id = user_id)
        new_account = accounts_model(user_id = user,
                                     phone = phone)
        new_account.save()


    def is_registered(self, user_id):
        return apps.get_model('tg_bot_app', 'Account').objects.filter(user_id=user_id)










