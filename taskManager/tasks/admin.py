from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'assigned_to')
    list_filter = ('completed','assigned_to')
    

admin.site.register(Task, TaskAdmin)