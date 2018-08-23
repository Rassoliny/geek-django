from django.shortcuts import render
from . import models
# Create your views here.
from django.shortcuts import HttpResponse


def main(request):
    return render(request, 'index.html', {})

def catalog(request):
    query = models.Product.objects.all()
    return render(request, 'catalog.html', {'results': query})


def contacts(request):
    return render(request, 'contacts.html', {})


def product_mirrow(request):
    return render(request, 'products/mirrow.html', {})


def product_box(request):
    return render(request, 'products/box.html', {})


def product_detail(request, pk):

    instance = models.Product.objects.get(id=pk)

    return render(request, 'products/detail.html', {'instance': instance})
