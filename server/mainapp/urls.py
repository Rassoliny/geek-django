from django.urls import re_path
from . import views as mainapp

app_name = 'products'

urlpatterns = [
    re_path(r'^$', mainapp.main, name='main'),
    re_path(r'products/(?P<pk>\d+)', mainapp.products, name='category'),
    re_path(r'(?P<pk>\d+)', mainapp.product_detail, name='product'),

]

