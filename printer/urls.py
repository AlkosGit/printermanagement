from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accos/', views.accos, name='accos'),
    path('acco/', views.acco, name='acco'),
    path('printers', views.printers, name='printers'),
    path('printer/', views.printer, name='printer'),
]