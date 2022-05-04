from django.core.management.base import BaseCommand, CommandError
from authorization.factories import AdminFactory, UserFactory


class Command(BaseCommand):
    help = "Seeds the database"

    def handle(self, *args, **options):
        print("🌱 Seeding local database")

        print("👤 Seeding Users")
        admin = AdminFactory(username="admin")
        user = UserFactory()

        print("✅ Done")
