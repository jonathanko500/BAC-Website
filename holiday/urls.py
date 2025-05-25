from django.urls import path
from . import views

app_name = 'holiday'

urlpatterns = [
    path('', views.holiday_view, name='holiday_view'),
    path('create/', views.create_holidays_view, name='create_holidays_view'),
    path('edit/<int:pk>/', views.edit_holiday_view, name='edit_holiday_view'),
    path('delete/<int:pk>/', views.delete_holiday_view, name='delete_holiday_view'),
]