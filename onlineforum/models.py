from django.db import models
import uuid

# Create your models here.
# Model for users
class CustomUser(models.Model):
    # Primary key for each user
    id = models.AutoField(primary_key=True)

    # Username of the user
    username = models.CharField(max_length=100)

    # Key
    key = models.CharField(max_length=100, default=uuid.uuid4, editable=False)

    # First Name of the user
    first_name = models.CharField(max_length=100)

    # Last Name of the user
    last_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.username} - ({self.first_name} {self.last_name})"

# Model for posts
class Post(models.Model):
    
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')

    msg = models.TextField()
    key = models.CharField(max_length=100, default=uuid.uuid4, editable=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        dt = self.timestamp.strftime("%d/%m/%Y %H:%M:%S")
        return f"{self.id} by {self.get_username()} at {dt}"
    
    def get_username(self):
        return self.user.username

