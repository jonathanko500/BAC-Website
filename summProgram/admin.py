
from django.contrib import admin
from .models import Program, Session, PageInfo

class SessionInline(admin.TabularInline):
    model = Session
    extra = 1

class ProgramAdmin(admin.ModelAdmin):
    inlines = [SessionInline]

admin.site.register(Program, ProgramAdmin)
admin.site.register(PageInfo)