import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Create the initial deployment admin from environment variables, if absent."

    def handle(self, *args, **options):
        username = os.environ.get("DJANGO_BOOTSTRAP_ADMIN_USERNAME", "").strip()
        email = os.environ.get("DJANGO_BOOTSTRAP_ADMIN_EMAIL", "").strip()
        password = os.environ.get("DJANGO_BOOTSTRAP_ADMIN_PASSWORD", "")

        values = (username, email, password)
        if not any(values):
            self.stdout.write("No bootstrap admin credentials configured; skipping.")
            return
        if not all(values):
            raise CommandError(
                "Set DJANGO_BOOTSTRAP_ADMIN_USERNAME, "
                "DJANGO_BOOTSTRAP_ADMIN_EMAIL, and DJANGO_BOOTSTRAP_ADMIN_PASSWORD together."
            )

        User = get_user_model()
        lookup = {User.USERNAME_FIELD: username}
        if User._default_manager.filter(**lookup).exists():
            self.stdout.write("Bootstrap admin already exists; leaving it unchanged.")
            return

        User._default_manager.create_superuser(
            username=username,
            email=email,
            password=password,
        )
        self.stdout.write("Bootstrap admin created.")
