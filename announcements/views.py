from django.shortcuts import render
from .models import Announcement, Department


def home(request):
    departments = Department.objects.all()
    announcements = Announcement.objects.filter(is_published=True).select_related("department")
    return render(
        request,
        "announcements/home.html",
        {"departments": departments, "announcements": announcements},
    )
