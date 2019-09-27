from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path("",views.shop,name="Shop"),
    path("products",views.product,name="Product")
]

