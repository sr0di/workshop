from django.contrib import admin

# Register your models here.
from manager.models import Task, Board


class TaskAdmin(admin.ModelAdmin):

    list_display = ['name', 'description', 'state']
    list_filter = ['state', 'board__user']


class BoardAdmin(admin.ModelAdmin):

    list_display = ['name', 'description', 'user']
    list_filter = ['user']


admin.site.register(Task, TaskAdmin)
admin.site.register(Board, BoardAdmin)
