# models.py

from django.db import models

# For Master Polo


class Coach(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    description = models.TextField()
    picture = models.ImageField(
        upload_to='uploads/coaches/masterPolo')  # Updated path

    def __str__(self):
        return self.name

# For Master Swim


class mCoachSwim(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    description = models.TextField()
    picture = models.ImageField(
        upload_to='uploads/coaches/mastersSwim')  # Updated path

    def __str__(self):
        return self.name

# For Age Group Polo


class compCoachPolo(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    description = models.TextField()
    picture = models.ImageField(
        upload_to='uploads/coaches/agPolo')  # Updated path

    def __str__(self):
        return self.name

# For Age Group Swim


class compCoachSwim(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    coaches_title = models.CharField(
        max_length=255, blank=True, null=True)
    description = models.TextField()
    picture = models.ImageField(
        upload_to='uploads/coaches/agSwim')  # Updated path

    def __str__(self):
        return self.name