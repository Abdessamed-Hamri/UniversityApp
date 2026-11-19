from django.contrib import admin
from .models import Announcement, Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name", "description")


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ("title", "department", "created_at", "is_published")
    list_filter = ("department", "is_published", "created_at")
    search_fields = ("title", "body")
