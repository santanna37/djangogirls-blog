from django.urls import path
from . import views 


# TODAS AS URLS 

urlpatterns = [
    path('', views.post_list, name='post_list')
]