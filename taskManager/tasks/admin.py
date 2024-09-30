from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'created_by', 'assigned_to')
    list_filter = ('completed', 'created_by')
    search_fields = ('title',)

admin.site.register(Task, TaskAdmin)