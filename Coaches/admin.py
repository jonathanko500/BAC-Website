# admin.py
from django.contrib import admin
from .models import Coach, mCoachSwim, compCoachPolo, compCoachSwim

admin.site.register(Coach)
admin.site.register(mCoachSwim)
admin.site.register(compCoachPolo)
admin.site.register(compCoachSwim)
