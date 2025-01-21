from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'is_completed', 'created_at')
    list_filter = ('priority', 'is_completed', 'created_at')
    search_fields = ('title', 'description')