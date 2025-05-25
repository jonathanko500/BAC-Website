"""
URL FOR LEGACY
"""
from django.urls import path
from . import views

app_name = 'legacy'

urlpatterns = [

    # ag polo records
    path('agPolo_records/', views.agPolo_records_view,
         name='agPolorecords'),

    path('add_agPolo_records/', views.add_agPolo_records,
         name='add_agPolo_records'),

    path('delete_agPolo_record/<int:record_id>/', views.delete_agPolo_record,
         name='delete_agPolo_record'),

    # ag polo alumni
    path('agPolo_alumni/', views.agPolo_alumni_view,
         name='agPoloalumni'),
    path('add_grad_polo/', views.add_grad_polo,
         name='add_agPoloalumni'),
    path('delete_grad_polo/<grad_name>', views.delete_grad_polo,
         name='delete_agPoloalumni'),
]
