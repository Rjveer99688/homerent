from django.urls import path,include
from .import views
from django.urls import re_path as url

app_name="homerent"
urlpatterns = [
    path('', views.my_form),
    url(r'form', views.my_form, name='form')
]
    