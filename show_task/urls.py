from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('show/', views.show_tasks, name='show_tasks'),
    path('complete/', views.complete_task, name='complete_task'),
    path('edit/', views.edit_task, name='edit_task'),
    
]
