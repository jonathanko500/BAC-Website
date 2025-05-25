from django.db import models

# Create your models here.


class aboutusEdit(models.Model):

    description = models.TextField(blank=True, null=True)

    AD_name = models.CharField(max_length=255, blank=True, null=True)

    AD_desc = models.TextField(blank=True, null=True)

    AD_pic = models.ImageField(
        upload_to='uploads/aboutus')

    PC_name = models.CharField(max_length=255, blank=True, null=True)

    PC_desc = models.TextField(blank=True, null=True)

    PC_pic = models.ImageField(
        upload_to='uploads/aboutus')


class jobDesc(models.Model):
    JOB_TYPE_CHOICES = [
        ('administration', 'Administration'),
        ('competitive', 'Competitive'),
        ('masters', 'Masters'),
        ('staff', 'Staff'),
    ]
    name = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Name of Job"
    )

    job_type = models.CharField(
        max_length=20,
        choices=JOB_TYPE_CHOICES,
        default='staff',
        verbose_name="Type of Job",
        blank=True,
        null=True
    )

    jobDesc_file = models.FileField(
        verbose_name="Dscription of Job",
        upload_to='uploads/aboutus/jobDesc'
    )
