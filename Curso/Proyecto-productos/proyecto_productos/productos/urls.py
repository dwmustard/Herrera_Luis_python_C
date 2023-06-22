from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [    
    path('index/', views.Index.as_view(), name = 'index')
]