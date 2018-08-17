"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import re_path
# from mainapp.views import mysite
import mainapp.views as mainapp


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', mainapp.main),
    re_path(r'^index', mainapp.main),
    re_path(r'^catalog', mainapp.catalog),
    re_path(r'^contacts', mainapp.contacts),
    re_path(r'^mirrow', mainapp.product_mirrow),
    re_path(r'^box', mainapp.product_box),
]
