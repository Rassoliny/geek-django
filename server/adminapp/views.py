from django.shortcuts import render, get_object_or_404
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product
from django.contrib.auth.decorators import user_passes_test


# Create your views here.

@user_passes_test(lambda u: u.is_superuser)
def users(request):
    title = 'admin/users'
    users_list = ShopUser.objects.all().order_by('-is_active', '-is_superuser',
                                                 '-is_sfaff', 'username')
    content = {
        'title': title,
        'objects': users_list
    }

    return render(request, 'adminapp/users.html', content)

def user_create(request):
    pass


def user_update(request, pk):
    pass


def user_delete(request, pk):
    pass


def categories(request):
    title = 'admin/categories'
    categories_list = ProductCategory.objects.all()

    content = {
        'title': title,
        'objects': categories_list,
    }

    return render(request, 'adminapp/categories.html', content)


def category_create(request):
    pass


def category_update(request, pk):
    pass


def category_delete(request, pk):
    pass


def products(request, pk):
    title = 'admin/products'
    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,

    }

    return render(request, 'adminapp/categories.html', content)


def product_create(request):
    pass


def product_update(request, pk):
    pass


def product_delete(request, pk):
    pass


def product_read(request, pk):
    pass