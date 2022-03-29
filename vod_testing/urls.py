from django import views
from django.urls import path
from vod_testing import views

urlpatterns = [
    path('test', views.test, name="test"),
    path('asset', views.asset, name="asset")
]
