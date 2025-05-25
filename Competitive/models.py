from django.db import models

# Create your models here.


class AGswimPage(models.Model):

    page_title = models.CharField(max_length=255, blank=True, null=True)

    page_subtitle = models.CharField(max_length=255, blank=True, null=True)

    urgent = models.TextField(blank=True, null=True)

    description_title = models.CharField(max_length=255, blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    practice_info_header = models.CharField(
        max_length=255, blank=True, null=True)

    practice_group_box_name = models.CharField(
        max_length=255, blank=True, null=True)

    practice_schedule_box_name = models.CharField(
        max_length=255, blank=True, null=True)

    swim_meet_header = models.CharField(max_length=255, blank=True, null=True)

    swim_meet_box_name = models.CharField(
        max_length=255, blank=True, null=True)

    new_members_title = models.CharField(max_length=255, blank=True, null=True)

    new_members_description = models.TextField(blank=True, null=True)

    current_members_title = models.CharField(
        max_length=255, blank=True, null=True)

    legacy_title = models.CharField(max_length=255, blank=True, null=True)

    records_description = models.TextField(blank=True, null=True)

    alumni_description = models.TextField(blank=True, null=True)


class AGswimEmail(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='uploads/coachesEmail/agSwim')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AGpoloPage(models.Model):

    urgent = models.TextField(blank=True, null=True)

    description = models.TextField(blank=True, null=True)

    new_members_description = models.TextField(blank=True, null=True)

    records_description = models.TextField(blank=True, null=True)

    alumni_description = models.TextField(blank=True, null=True)

    polo_registration_link = models.URLField(blank=True, null=True)


class AGpoloEmail(models.Model):
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to='uploads/coachesEmail/agPolo')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title