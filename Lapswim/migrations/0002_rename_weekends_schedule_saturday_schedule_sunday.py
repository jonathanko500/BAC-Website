# Generated by Django 4.2.4 on 2023-10-12 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lapswim', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='schedule',
            old_name='weekends',
            new_name='saturday',
        ),
        migrations.AddField(
            model_name='schedule',
            name='sunday',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
