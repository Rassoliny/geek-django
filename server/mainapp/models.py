from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    short_description = models.TextField(blank=True, max_length=300)
    description = models.TextField(blank=True, max_length=500)

    def __str__(self):

        return self.title