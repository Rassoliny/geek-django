from django.shortcuts import render, get_object_or_404
from . import models
from basketapp.models import Basket
import random
# Create your views here.
from django.shortcuts import HttpResponse


def main(request):
    products = models.Product.objects.all()[:4]

    content = {'products': products}
    return render(request, 'mainapp/index.html', content)


def catalog(request):
    query = models.Product.objects.all()
    return render(request, 'mainapp/catalog.html', {'results': query})


def contacts(request):
    return render(request, 'mainapp/contacts.html', {})


def product_mirrow(request):
    return render(request, 'products/mirrow.html', {})


def product_box(request):
    return render(request, 'products/box.html', {})


def product_detail(request, pk):
    instance = models.Product.objects.get(id=pk)
    return render(request, 'products/detail.html', {'instance': instance})


def get_basket(user):
    if user.is_authenticated:
        return Basket.objects.filter(user=user)
    else:
        return []


def get_hot_products():
    products = models.Product.objects.all()

    return random.sample(list(products), 1)[0]


def get_same_products(hot_product):
    same_products = models.Product.objects.filter(category=hot_product.category).exclude(pk=hot_product.pk)[:3]
    return same_products


def products(request, pk=None):
    title = 'Продукты'
    links_menu = models.ProductCategory.objects.all()

    if pk:
        if pk == '0':
            category = {'name': 'все'}
            products = models.Product.objects.all().order_by('cost')
        else:
            category = get_object_or_404(models.ProductCategory, pk=pk)
            products = models.Product.objects.filter(category__pk=pk).order_by('cost')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
        }

        return render(request, 'mainapp/products_list.html', content)

    hot_product = get_hot_products()
    same_products = get_same_products(hot_product)


    content = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,

    }

    return render(request, 'mainapp/products.html', content)
