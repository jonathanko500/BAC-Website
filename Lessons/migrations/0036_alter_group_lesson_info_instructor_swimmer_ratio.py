# Generated by Django 4.2.4 on 2024-03-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lessons', '0035_group_lesson_info_ages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group_lesson_info',
            name='instructor_swimmer_ratio',
            field=models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=1, null=True, verbose_name='Instructor/Swimmer ratio'),
        ),
    ]
