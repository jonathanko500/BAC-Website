"""
URL FOR ABOUTUS
"""

from django.urls import path
from . import views

app_name = 'aboutus'

urlpatterns = [
    # job desc page
    path('jobDesc/', views.jobDesc_view, name='jobDesc'),
    path('jobDesc/create/', views.jobDesc_create_view, name='jobDesc_create'),
    path('jobDesc/delete/<int:job_id>/',
         views.delete_job_desc, name='jobDesc_delete'),
    # about us page
    path('aboutus/', views.aboutus_view, name='aboutus'),
    path('edit_aboutus/', views.edit_aboutus, name='edit_aboutus'),
]
