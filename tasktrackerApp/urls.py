from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'tasktrackerApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_task', views.add_task, name='add_task'),
    path('add_worker/', views.add_worker, name='add_worker'),
    path('list_workers/', views.list_workers, name='list_workers'),
    path('update_items/<str:pk>/', views.update_items, name='update_items'),
    path('delete_worker/<str:pk>/', views.delete_worker, name='delete_worker'),
]
