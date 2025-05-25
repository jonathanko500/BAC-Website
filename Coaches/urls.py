"""
URL FOR COACHES
"""
from django.urls import path
from . import views

app_name = 'coaches'

urlpatterns = [
    path('masters_swim_coaches/', views.masters_swim_coaches_view,
         name='mastersSwimCoaches'),
    path('add_coach_swim/', views.add_coach_swim,
         name='addCoachSwim'),  # For Master Swim
    path('delete_coach_swim/<coach_name>', views.delete_coach_swim,
         name='deleteCoachSwim'),  # For Master Swim

    path('masters_polo_coaches/', views.masters_polo_coaches_view,
         name='mastersPoloCoaches'),
    path('add_coach/', views.add_coach,
         name='addCoach'),  # For Master Polo
    path('delete_coach_polo/<coach_name>', views.delete_coach_polo,
         name='deleteCoachPolo'),  # For Master Polo

    path('AG_polo_coaches/', views.AG_polo_coaches_view, name='AGPoloCoaches'),
    path('add_AG_polo_coaches/', views.add_AG_polo_coaches,
         name='addAGpolocoaches'),  # For AG Polo
    path('delete_AG_polo_coaches/<coach_name>', views.delete_AG_polo_coaches,
         name='deleteAGPoloCoach'),  # For AG Polo


    path('AG_swim_coaches/', views.AG_swim_coaches_view, name='AGSwimCoaches'),
    path('add_AG_swim_coaches/', views.add_AG_swim_coaches,
         name='addAGswimcoaches'),  # For AG Swim
    path('delete_AG_swim_coaches/<coach_name>', views.delete_AG_swim_coaches,
         name='deleteAGSwimCoach'),  # For AG Swim
]