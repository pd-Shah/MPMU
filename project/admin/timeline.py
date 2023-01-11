from django.contrib import admin

from ..models import TimeLine

BASE = ["title", "description", "created_at", "updated_at", ]


@admin.register(TimeLine)
class TimeLineAdmin(admin.ModelAdmin):
    list_filter = [] + BASE
    list_display = [] + BASE
