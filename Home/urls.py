from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),  # Define a view for the root path
    path('edit_homePage/', views.edit_homePage, name='edit_homePage'),

]
