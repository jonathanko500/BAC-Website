# Generated by Django 4.2.4 on 2023-09-17 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lessons', '0015_alter_privateschedule_lesson1_age_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='privateschedule',
            name='registraion_heading',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='privateschedule',
            name='registraion_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
