from django.shortcuts import render, get_object_or_404
from . import models
from basketapp.models import Basket
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

def products(request, pk):
    print(pk)

    title = 'Продукты'
    links_menu = models.ProductCategory.objects.all()

    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

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
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)

    same_products = models.Product.objects.all()[3:5]

    content = {
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,

    }

    return render(request, 'mainapp/products.html', content)
