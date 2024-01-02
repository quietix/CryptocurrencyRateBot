from django.db import models


class Users(models.Model):
    UserID = models.IntegerField(primary_key=True)
    Name = models.CharField()
    Surname = models.CharField()
    Username = models.CharField()


class Accounts(models.Model):
    UserID = models.IntegerField(primary_key=True)
    Phone = models.CharField(max_length=12)