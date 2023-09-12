from django.contrib import admin

from .models import Tasks
from .models import Category


class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'due_date')


admin.site.register(Tasks, TasksAdmin)
admin.site.register(Category)
