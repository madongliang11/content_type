from django.contrib import admin
from django.urls import path
from django.conf.urls import url

from app01 import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'test/$', views.test),
]
