# Generated by Django 4.2.4 on 2024-08-07 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus', '0005_alter_jobdesc_jobdesc_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobdesc',
            name='job_type',
            field=models.CharField(blank=True, choices=[('administration', 'Administration'), ('competitive', 'Competitive'), ('masters', 'Masters'), ('staff', 'Staff')], default='staff', max_length=20, null=True, verbose_name='Type of Job'),
        ),
    ]
