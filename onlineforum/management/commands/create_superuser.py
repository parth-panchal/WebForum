from django.core.management.base import (
    BaseCommand,
    CommandError
)

from onlineforum.models import CustomUser

from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Creates superuser'

    def handle(self, *args, **options):
        # Check if data already exists
        if User.objects.exists():
            self.stdout.write("Data already exists. Skipping data creation.")
            return

        try:
            User.objects.create_superuser(
                username='harvish',
                password='abcd',
                )
            
            self.stdout.write("Superuser created successfully")

            CustomUser.objects.create(
                username='harvish',
                first_name='Harvish',
                last_name='Jariwala',
                )
        except Exception as e:
            raise CommandError(e)