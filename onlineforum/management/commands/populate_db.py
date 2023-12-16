from django.core.management.base import (
    BaseCommand,
    CommandError
)

from onlineforum.models import CustomUser, Post

class Command(BaseCommand):
    help = 'Creates users and posts'

    def handle(self, *args, **options):
        # Check if data already exists
        if CustomUser.objects.exists() or Post.objects.exists():
            self.stdout.write("Data already exists. Skipping data creation.")
            return

        
        try:
            users = [
                {
                    'username': 'user1',
                    'first_name': 'User1',
                    'last_name': 'One'
                },
                {
                    'username': 'user2',
                    'first_name': 'User2',
                    'last_name': 'Two'
                },
                {
                    'username': 'user3',
                    'first_name': 'User3',
                    'last_name': 'Three'
                },
                {
                    'username': 'user4',
                    'first_name': 'User4',
                    'last_name': 'Four'
                },
                {
                    'username': 'user5',
                    'first_name': 'User5',
                    'last_name': 'Five'
                },
            ]

            users = [CustomUser(**user) for user in users]
            CustomUser.objects.bulk_create(users)

            # Create posts
            posts = [
                {
                    'user_id': 1,
                    'msg': 'Hello World!'
                },
                {
                    'user_id': 1,
                    'msg': 'This is a test post'
                },
                {
                    'user_id': 2,
                    'msg': 'This is another test post'
                },
                {
                    'user_id': 3,
                    'msg': 'This is yet another test post'
                },
            ]

            Post.objects.bulk_create([Post(**post) for post in posts])
        except Exception as exec:
            self.stderr.write(f"Error while creating users and posts: {exec}")
            raise CommandError(f"Error while creating users and posts: {exec}")