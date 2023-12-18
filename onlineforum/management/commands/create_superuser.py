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
                username='admin',
                password='admin',
                )
            
            self.stdout.write("Superuser created successfully")

            CustomUser.objects.create(
                username='nancyradadia',
                first_name='Nancy',
                last_name='Radadia',
                )
        except Exception as e:
            raise CommandError(e)