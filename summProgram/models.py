from django.db import models

class Program(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    class_duration = models.TextField(blank=True, null=True)
    fee = models.DecimalField(max_digits=6, decimal_places=2, verbose_name = "Weekday Fee")
    weekend_fee = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fee_note = models.TextField(blank=True, null=True, verbose_name = "Program Notes")
    number_of_sessions = models.PositiveIntegerField()
    number_of_weekend_sessions = models.PositiveIntegerField(default=0)  # New field for weekend sessions
    picture = models.ImageField(upload_to='uploads/summerProgram', blank=True, null=True)

    def __str__(self):
        return self.title

class Session(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='sessions')
    start_date = models.DateField()
    end_date = models.DateField()
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.program.title} ({self.start_date} - {self.end_date})"

class WeekendSession(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='weekend_sessions')
    start_date = models.DateField()
    end_date = models.DateField()
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.program.title} ({self.start_date} - {self.end_date})"

class PageInfo(models.Model):
    urgent = models.TextField(blank=True, null=True)
    recswim_info = models.TextField(blank=True, null=True)
    weekdays = models.CharField(max_length=255, blank=True, null=True, verbose_name="Weekdays Schedule for Recswim")
    weekdays_timeframe = models.CharField(max_length=255, blank=True, null=True)
    weekends = models.CharField(max_length=255, blank=True, null=True, verbose_name="Weekends Schedule for Recswim")
    weekends_timeframe = models.CharField(max_length=255, blank=True, null=True)
    daily_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    registration_info = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='uploads/summerProgram', blank=True, null=True, verbose_name="Recswim image")
