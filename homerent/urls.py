from django.urls import path,include
from .import views
from django.urls import re_path as url
from django.conf import settings
from django.conf.urls.static import static

app_name="homerent"
urlpatterns = [
    path('', views.home),
    path('home/',views.home, name="home"),
    path('eunit/',views.eunit,name="eunit"),
    path('payment/',views.payment,name="payment")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    