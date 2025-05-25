from django.db import models

class homePage(models.Model):
    announcement = models.TextField(blank=True, null=True)
    show_download_link = models.BooleanField(
        default=False,verbose_name="Display Summer Program Info")
