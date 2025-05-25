"""
URL FOR MASTERS
"""

from django.urls import path
from . import views

app_name = 'masters'

urlpatterns = [

    path('masters_swim/', views.masters_swim_view, name='mastersSwim'),
    path('edit_swim_schedule/', views.edit_swim_schedule,
         name='edit_swim_schedule'),

    path('masters_polo/', views.masters_polo_view, name='mastersPolo'),
    path('edit_polo_schedule/', views.edit_polo_schedule,
         name='edit_polo_schedule'),
]
