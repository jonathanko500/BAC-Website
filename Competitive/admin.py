from django.contrib import admin
from .models import AGswimPage, AGpoloPage, AGswimEmail, AGpoloEmail

# Register your models here.
admin.site.register(AGswimPage)
admin.site.register(AGpoloPage)
admin.site.register(AGswimEmail)
admin.site.register(AGpoloEmail)