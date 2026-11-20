from django.shortcuts import render
from .models import Announcement, Department


def home(request):
    return render(request, "announcements/home.html")


def departments_page(request):
    departments = Department.objects.all()
    return render(
        request,
        "announcements/departments.html",
        {"departments": departments},
    )


def announcements_page(request):
    announcements = Announcement.objects.filter(is_published=True).select_related("department")
    return render(
        request,
        "announcements/announcements.html",
        {"announcements": announcements},
    )
