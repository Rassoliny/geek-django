from django.db import models
from django.conf import settings
from mainapp.models import Product

# Create your models here.
class Basket(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='Количество', default=0)
    add_datetime = models.DateTimeField(verbose_name='Время', auto_now_add=True)


    def _get_product_cost(self):
        return self.product.cost * self.quantity


    def _get_total_quantity(self):
        _items = Basket.objects.filter(user=self.user)
        _totalquantity = sum(list(map(lambda x: x.quantity, _items)))
        return _totalquantity

    total_quantity = property(_get_total_quantity)

    def _get_total_cost(self):
        _items = Basket.objects.filter(user=self.user)
        _totalcost = sum(list(map(lambda x: x.product.cost, _items)))
        return _totalcost

    total_cost = property(_get_total_cost)

    @staticmethod
    def get_items(user):
        return user.basket_set.all()