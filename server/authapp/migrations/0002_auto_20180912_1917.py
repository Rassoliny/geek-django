# Generated by Django 2.1.1 on 2018-09-12 19:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='activation_key',
            field=models.CharField(blank=True, max_length=128, verbose_name='ключ подтверждения'),
        ),
        migrations.AddField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2018, 9, 14, 19, 17, 30, 162297, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
