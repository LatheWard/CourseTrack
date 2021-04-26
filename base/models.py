from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# user model
class The_User(AbstractUser):
    coursesTaken = models.PositiveIntegerField