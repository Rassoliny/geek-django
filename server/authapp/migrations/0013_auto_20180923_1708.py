# Generated by Django 2.1.1 on 2018-09-23 17:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0012_auto_20180916_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 25, 17, 8, 9, 148941, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
