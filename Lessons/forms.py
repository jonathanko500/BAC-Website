from django import forms
from .models import PrivateSchedule, SwimLessons, lessonInfoHome, Group_Lesson_Info


class Swim_LessonForm(forms.ModelForm):
    class Meta:
        model = SwimLessons
        fields = '__all__'  # This includes all fields from your model in the form


class lessonInfoHomeForm(forms.ModelForm):
    class Meta:
        model = lessonInfoHome
        fields = '__all__'  # This includes all fields from your model in the form


class Group_Lesson_InfoForm(forms.ModelForm):
    class Meta:
        model = Group_Lesson_Info
        fields = '__all__'  # This includes all fields from your model in the form


class PrivateScheduleForm(forms.ModelForm):
    class Meta:
        model = PrivateSchedule
        fields = '__all__'  # This includes all fields from your model in the form
