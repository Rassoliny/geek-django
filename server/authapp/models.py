from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
from datetime import timedelta


def get_activation_key_expires():
    return now() + timedelta(hours=48)

class ShopUser(AbstractUser):
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name='возраст')

    activation_key = models.CharField(verbose_name='ключ подтверждения', max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(
        verbose_name='актуальность ключа',
        default=get_activation_key_expires

    def is_activation_key_expired(self):
        if now() <= self.activation_key_expires:
            return False
        else:
            return True