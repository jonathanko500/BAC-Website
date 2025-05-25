"""
URL FOR COMP
"""

from django.urls import path
from . import views

app_name = 'competitive'

urlpatterns = [
    path('comp_swim/', views.comp_swim_view, name='compSwim'),
    path('edit_comp_swim/', views.edit_comp_swim, name='compSwimEdit'),
    path('upload_pdf_swim/', views.upload_pdf_swim, name='upload_pdf_swim'),
    path('download_pdf_swim/<int:pdf_id>/',
         views.download_pdf_swim, name='download_pdf_swim'),
    path('comp_polo/', views.comp_polo_view, name='compPolo'),
    path('edit_comp_polo/', views.edit_comp_polo, name='compPoloEdit'),
    path('upload_pdf_polo/', views.upload_pdf_polo, name='upload_pdf_polo'),
    path('download_pdf_polo/<int:pdf_id>/',
         views.download_pdf_polo, name='download_pdf_polo'),
]