from django.db import models

# Create your models here.


class Grad(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    college = models.CharField(max_length=255, blank=True, null=True)
    picture = models.ImageField(
        upload_to='uploads/legacy/agPolo')  # Updated path

    def __str__(self):
        return self.name


class AgeTeam(models.Model):
    name = models.CharField(max_length=100, primary_key=True)


class agPolo_Record(models.Model):
    age_of_team = models.ForeignKey(AgeTeam, on_delete=models.CASCADE)
    type_of_team = models.CharField(max_length=255, blank=True, null=True)
    tournament = models.CharField(max_length=255, blank=True, null=True)
    placement = models.CharField(max_length=255, blank=True, null=True)
    season = models.CharField(max_length=255, blank=True, null=True)
