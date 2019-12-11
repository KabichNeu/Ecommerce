"""webapps URL Configuration

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
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from registration import views
from django.conf import settings
from django.conf.urls.static import static




 
from products.views import (ProductDetailSlugView,ProductFeaturedDetailView,ProductFeaturedListView,ProductListView,product_list_view,product_detail_view,ProductDetailView)


urlpatterns = [

    path('admin/', admin.site.urls),
    path('',views.eshop,name='eshop'),
    path('registration/', include('registration.urls')),
    path('logout/',views.user_logout,name='logout'),
    path('special/',views.special,name='special '),
    path('feature/', ProductFeaturedListView.as_view()),
    re_path('featured/(?P<pk>\d+)/', ProductFeaturedDetailView.as_view()),
    path('product/', include("products.urls")),

    # path('product/', ProductListView.as_view()),
    # path('products-fbv/',product_list_view),
    # re_path('product/(?P<pk>\d+)/', ProductDetailView.as_view()),
    # path('products/(?P<slug>[\w-]+)/',ProductDetailSlugView.as_view()),
    # re_path('products-fbv/(?P<pk>\d+)/', product_detail_view),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
