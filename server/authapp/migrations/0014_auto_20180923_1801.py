# Generated by Django 2.1.1 on 2018-09-23 18:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0013_auto_20180923_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 25, 18, 1, 26, 471987, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
