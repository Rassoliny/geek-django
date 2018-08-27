from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
from django.contrib.auth.models import User
import json, os



super_user = User.objects.create_superuser('adm', 'adm@kovashop.local', 'qwe123', age = 25)