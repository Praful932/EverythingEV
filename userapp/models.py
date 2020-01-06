from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    is_consumer = models.BooleanField('consumer status',default=False)
    is_provider = models.BooleanField('provider status',default=False)
    def __str__(self):
        return self.username