# Generated by Django 2.1.1 on 2018-09-14 03:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0002_auto_20180912_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 16, 3, 29, 51, 379573, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
