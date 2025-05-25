"""
URL FOR LESSONS
"""

from django.urls import path
from . import views
from .views import GroupLessonInfoDeleteView


app_name = 'lessons'

urlpatterns = [
    # page views
    path('swim_lessons/', views.swim_lessons,
         name='swim_lessons'),  # home swim lesson

    path('lesson_info/', views.lessonInfoHome_view,
         name='lessonInfo'),  # home lesson info

    path('private/', views.private_view, name='private'),  # private lesson

    # start edit views
    path('edit_swim_lessons/', views.edit_swim_lessons,
         name='edit_swim_lessons'),  # edit home swim lesson


    path('edit_lessonInfo/', views.edit_lessonInfoHome_view,  # edit home lesson info
         name='edit_lessonInfo'),
    path('add_lessonInfo/', views.edit_GroupDetailInfo_view,  # add lesson info
         name='add_lessonInfo'),
    path('lesson-info/delete/<int:pk>/',  # delee lesson info
         GroupLessonInfoDeleteView.as_view(), name='delete-lesson-info'),

    path('edit_private/', views.edit_private,
         name='edit_private'),  # edit private lesson
]
