"""
URLS FOR LAPSWIM
"""

from django.urls import path
from . import views

app_name = 'lapswim'

urlpatterns = [
    path('', views.index, name='index'),
    path('edit_schedule/', views.edit_schedule, name='edit_schedule'),

]
