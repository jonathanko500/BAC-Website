from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Holiday(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('adjusted', 'Adjusted Schedule'), ('closed', 'Closed'), ('regular', 'Regular Schedule')])
    scheduled_time = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

    def clean(self):
        # if self.status == 'closed' and self.scheduled_time:
        #     raise ValidationError('Scheduled time should not be set if the status is closed.')
        if self.status == 'adjusted' and not self.scheduled_time:
            raise ValidationError('Scheduled time is required if the status is adjusted.')