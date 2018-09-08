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
from django.urls import path, include
from django.urls import re_path
from django.conf.urls.static import static
from django.conf import settings
import mainapp.views as mainapp



urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', mainapp.main, name='main'),
    # re_path(r'^index', mainapp.main, name=''),
    re_path(r'^catalog', mainapp.catalog, name='catalog'),
    re_path(r'^contacts', mainapp.contacts, name='contacts'),
    re_path(r'^mirrow', mainapp.product_mirrow, name='mirrow'),
    re_path(r'^box', mainapp.product_box, name='box'),
    re_path(r'(?P<pk>\d+)', mainapp.product_detail, name='detail'),
    re_path(r'^auth', include('authapp.urls')),
    re_path(r'^products', include('mainapp.urls', namespace='products')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
