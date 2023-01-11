from django.contrib import admin

from ..models import Project

BASE = ["title", "description", "created_at", "updated_at", ]


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_filter = [] + BASE
    list_display = [] + BASE
