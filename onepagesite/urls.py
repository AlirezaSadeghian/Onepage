from django.urls import path 
from .views import *

app_name = 'onepagesite'

urlpatterns = [
    path("",home),
]
