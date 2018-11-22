from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('accos/', views.accos, name='accos'),
    path('accos/<int:acco_id>', views.acco, name='acco'),
    path('printers', views.printers, name='printers'),
    path('printers/<int:printer_id>', views.printer, name='printer'),
]