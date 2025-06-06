# Generated by Django 5.1.5 on 2025-02-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_alter_homepage_show_download_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='popup',
            name='display_status',
            field=models.BooleanField(default=False, verbose_name='Display Pop Up'),
        ),
        migrations.AlterField(
            model_name='popup',
            name='file_status',
            field=models.BooleanField(default=False, verbose_name='Provide a Downloadable File'),
        ),
    ]
