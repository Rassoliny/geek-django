from django.shortcuts import render
from . import models
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