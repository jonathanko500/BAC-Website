# Generated by Django 4.2.4 on 2024-02-29 03:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Lessons', '0033_group_lesson_info_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessoninfohome',
            name='location_of_advanced_lessons',
        ),
        migrations.RemoveField(
            model_name='lessoninfohome',
            name='location_of_beginner_lessons',
        ),
    ]
