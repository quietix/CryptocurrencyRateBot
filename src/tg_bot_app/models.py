from django.db import models
import random


class User(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255, null=True)
    surname = models.CharField(max_length=255, null=True)
    username = models.CharField(max_length=255, null=True)
    def __str__(self):
        return f'{self.user_id}'


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    phone = models.CharField(max_length=255, null=False)
    def __str__(self):
        return f'{self.account_id}'


class Admin(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)