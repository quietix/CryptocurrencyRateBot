# Generated by Django 5.0.1 on 2024-01-04 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_bot_app', '0002_remove_user_id_alter_user_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]