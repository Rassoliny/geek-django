# Generated by Django 2.1.1 on 2018-09-09 03:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('short_desc', models.CharField(blank=True, max_length=200, verbose_name='краткое описание')),
                ('description', models.TextField(blank=True, verbose_name='подбробное описание')),
                ('publicated', models.CharField(choices=[('PUB', 'Publicated'), ('PRV', 'Private')], default='PUB', max_length=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modifield', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя')),
                ('description', models.TextField(blank=True, verbose_name='описание')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory'),
        ),
    ]