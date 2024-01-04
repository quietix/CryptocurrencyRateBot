from django.db import models


class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    username = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    phone = models.CharField(max_length=12, null=False)

    def __str__(self):
        return f"AccountID={self.account_id}, {User}"