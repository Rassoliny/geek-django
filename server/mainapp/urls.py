from django.urls import re_path
from . import views as mainapp

app_name = 'products'

urlpatterns = [
    re_path(r'category/(?P<pk>\d+)/page/(?P<page>\d+)', mainapp.products, name='page'),
    re_path(r'products/(?P<pk>\d+)', mainapp.products, name='category'),
    re_path(r'(?P<pk>\d+)', mainapp.product_detail, name='product'),
    re_path(r'^$', mainapp.main, name='main'),

]

