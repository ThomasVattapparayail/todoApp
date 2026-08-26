from django.contrib import admin
from .models import todo

# Register your models here.

@admin.register(todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'todo', 'todo_dis', 'done')