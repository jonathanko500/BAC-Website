"""
URL FOR RECSWIM
"""
from django.urls import path
from . import views

app_name = 'recswim'  # Define the namespace for the app

urlpatterns = [
    path('', views.index, name='index'),
    path('edit_schedule/', views.edit_schedule, name='edit_schedule'),

]
