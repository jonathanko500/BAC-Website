from django.contrib import admin
from .models import PrivateSchedule, SwimLessons, lessonInfoHome, Group_Lesson_Info
# Register your models here.

admin.site.register(PrivateSchedule)
admin.site.register(SwimLessons)
admin.site.register(lessonInfoHome)
admin.site.register(Group_Lesson_Info)
