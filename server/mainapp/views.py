from django.shortcuts import render, get_object_or_404
from . import models
from basketapp.models import Basket
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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


def products(request, pk=None, page=1):
    title = 'Продукты'
    links_menu = models.ProductCategory.objects.filter(is_active=True)

    if pk:
        if pk == '0':
            category = {
                'pk': 0,
                'name': 'все'
            }
            products = models.Product.objects.filter(is_active=True, category__is_active=True).order_by('cost')
        else:
            category = get_object_or_404(models.ProductCategory, pk=pk)
            products = models.Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True
                                                     ).order_by('cost')

        paginator = Paginator(products, 2)
        try:
            products_paginator = paginator.page(page)
        except PageNotAnInteger:
            products_paginator = paginator.page(1)
        except EmptyPage:
            products_paginator = paginator.page(paginator.num_pages)
        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products_paginator
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
