from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)

    def __str__(self):

        return self.name

class Product(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2)


    def __str__(self):

        return self.title