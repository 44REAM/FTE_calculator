from django.contrib import admin

from .models import WorkLoad

class WorkLoadAdmin(admin.ModelAdmin):
    list_display  = ('pk','opd', 'ipd','er', 'icu','labour')
# Register your models here.
admin.site.register(WorkLoad, WorkLoadAdmin)
