# Generated by Django 4.2.4 on 2023-09-18 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Legacy', '0005_delete_agpolo_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='ag_polo_record',
            fields=[
                ('age_of_team', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('type_of_team', models.CharField(blank=True, max_length=255, null=True)),
                ('tournament', models.CharField(blank=True, max_length=255, null=True)),
                ('placement', models.CharField(blank=True, max_length=255, null=True)),
                ('season', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
