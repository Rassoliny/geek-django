from django.shortcuts import render
from . import models
# Create your views here.
from django.shortcuts import HttpResponse


def main(request):
    query = models.Product.objects.all()
    return render(request, 'index.html', {'results': query})

def catalog(request):
    return render(request, 'catalog.html', {})


def contacts(request):
    return render(request, 'contacts.html', {})


def product_mirrow(request):
    return render(request, 'products/mirrow.html', {})


def product_box(request):
    return render(request, 'products/box.html', {})
