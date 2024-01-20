from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("", views.index, name="MyApp"),
    path("menu/", views.menu, name="MyApp"),
    path("about/", views.about, name="MyApp"),
    path("contact/", views.contact, name="MyApp"),
]
