from django.core.management.base import BaseCommand
from mainapp.models import ProductCategory, Product
# from django.contrib.auth.models import User
from authapp.models import ShopUser
import json, os


class Command(BaseCommand):
    def handle(self, *args, **options):
        super_user = ShoUser.objects.create_superuser('adm', 'adm@kovashop.local', 'qwe123', age = 25)