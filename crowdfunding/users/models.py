from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    first_name = models.TextField(max_length=30, blank=True)
    last_name = models.TextField(max_length=30, blank=True)
    location = models.TextField(max_length=30, blank=True)
    image = models.TextField(default="https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/golden-retriever-royalty-free-image-506756303-1560962726.jpg")
    about_me = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return self.username


