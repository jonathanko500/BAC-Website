from django.urls import path
from . import views

app_name = 'summProgram'

urlpatterns = [
    path('', views.summProgram_view, name='summProgram'),
    path('add_program_and_sessions/', views.add_program_and_sessions_view, name='addProgramAndSessions'),
    path('edit_program/<int:program_id>/', views.edit_program_view, name='editProgram'),
    path('delete_program/<int:program_id>/', views.delete_program_view, name='deleteProgram'),
    path('edit_page_info/', views.edit_page_info_view, name='editPageInfo'),  # New URL pattern
]