from django.db import models

# Create your models here.


class Product(models.Model):
    PUBLICATED = 'PUB'

    PRIVATE = 'PRV'

    PUBLICATED_CHOICES = (
        (PUBLICATED, 'Publicated'),
        (PRIVATE, 'Private'),
    )

    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    short_description = models.TextField(blank=True, max_length=300)
    description = models.TextField(blank=True, max_length=500)

    publicated = models.CharField(
        max_length=3,
        choices=PUBLICATED_CHOICES,
        default=PUBLICATED
    )

    created = models.DateTimeField(auto_now_add=True)

    modifield = models.DateTimeField(auto_now=True)

    def __str__(self):

        return self.title