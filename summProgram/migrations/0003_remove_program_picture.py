# Generated by Django 5.1.5 on 2025-01-26 01:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summProgram', '0002_program_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='program',
            name='picture',
        ),
    ]
