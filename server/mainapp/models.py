from django.db import models

# Create your models here.

class ProductCategory(models.Model):
    name = models.CharField(verbose_name='имя', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    is_active = models.BooleanField(verbose_name='активна', default=True)

    def __str__(self):

        return self.name

class Product(models.Model):

    PUBLICATED = 'PUB'

    PRIVATE = 'PRV'

    PUBLICATED_CHOICES = (
        (PUBLICATED, 'Publicated'),
        (PRIVATE, 'Private'),
    )

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    short_desc = models.CharField(verbose_name='краткое описание', max_length=200, blank=True)
    description = models.TextField(verbose_name='подбробное описание', blank=True)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    publicated = models.CharField(
        max_length=3,
        choices=PUBLICATED_CHOICES,
        default=PUBLICATED
    )
    created = models.DateTimeField(auto_now_add=True)
    modifield = models.DateTimeField(auto_now=True)


    def __str__(self):

        return self.title