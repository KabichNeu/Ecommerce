
from django.urls import path,re_path
from registration import views
from django.conf import settings
from products.views import (
                            ProductDetailSlugView
                        #    ,ProductFeaturedDetailView
                        #    ,ProductFeaturedListView
                        #    ,ProductListView
                        #    ,product_list_view
                        #    ,product_detail_view
                        #    ,ProductDetailView)

urlpatterns = [
    path('', ProductListView.as_view()),
    path('(?P<slug>[\w-]+)/',ProductDetailSlugView.as_view()),

] 