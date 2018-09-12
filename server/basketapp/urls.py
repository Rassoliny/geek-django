from django.urls import path, re_path
from . import views as baskethapp

app_name = 'basket'


urlpatterns = [
    re_path(r'^$', baskethapp.basket, name='view'),
    re_path(r'^add/(?P<pk>\d+)', baskethapp.basket_add, name='add'),
    re_path(r'^remove/(?P<pk>\d+)', baskethapp.basket_remove, name='remove'),
    re_path(r'^edit/(?P<pk>\d+)/(?P<quantity>\d+)', baskethapp.basket_edit, name='edit'),

]

