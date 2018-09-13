from django.shortcuts import render, get_object_or_404
from authapp.model import ShopUser
from mainapp.model import ProductCategory, Product


# Create your views here.


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