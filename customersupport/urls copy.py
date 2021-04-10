"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler400, handler404, handler500
from django.conf import settings

from Ecommerce.settings import INSTALLED_APPS

# if settings.ADMIN_ENABLED is True:
#     INSTALLED_APPS.append('django.contrib.admin')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('UserDetails.urls')),
    path('product/', include('ProductDetails.urls')),
    path('customers/', include('CustomerDetails.urls')),
    path('cart/', include('CartDetails.urls')),
    path('discount/', include('Discounts.urls')),
    path('mailer/', include('Mailer.urls')),
    path('orders/', include('Orders.urls')),
    path('ship/', include('shiprocket.urls')),
    path('catalogue/', include('Catalogue.urls')),
    path('invoice/', include('Invoice.urls')),
    path('discount-module/', include('DiscountModule.urls')),


]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
handler404 = 'Ecommerce.views.bad_request'