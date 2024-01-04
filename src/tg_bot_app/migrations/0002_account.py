# Generated by Django 5.0.1 on 2024-01-04 09:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg_bot_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=12)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tg_bot_app.user')),
            ],
        ),
    ]