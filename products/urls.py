
from django.urls import path,re_path
from registration import views
from django.conf import settings
from products.views import ProductDetailSlugView,ProductListView,charge

                        #    ,ProductFeaturedDetailView
                        #    ,ProductListView
                        #    ,product_list_view
                        #    ,product_detail_view
                        #    ,ProductDetailView)

app_name="products"
urlpatterns = [
    path('', ProductListView.as_view(),name='list'),
    path('(?P<slug>[\w-]+)/',ProductDetailSlugView.as_view(),name='detail'),
    

] 