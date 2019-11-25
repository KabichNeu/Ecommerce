from django.urls import path
from registration import views

#TEMPLATE TAGGING
app_name = 'registration'


urlpatterns=[
    path('register/',views.register,name='register'),
    path('user_login/',views.user_login,name='user_login'),
]