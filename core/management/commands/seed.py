from django.core.management.base import BaseCommand, CommandError
from authorization.factories import AdminFactory


class Command(BaseCommand):
    help = "Seeds the database"

    def handle(self, *args, **options):
        print("🌱 Seeding local database")

        print("👤 Seeding Users")
        admin = AdminFactory(username="admin")

        print("✅ Done")
