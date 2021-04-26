from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# user model
class The_User(AbstractUser):
    coursesTaken = models.PositiveIntegerField(null=True, blank=True)

class Course(models.Model):
    title = models.TextField
    startDate = models.DateField
    endDate = models.DateField
    description = models.TextField
    size = models.PositiveIntegerField
    avalability = models.PositiveIntegerField

class UserGrade(models.Model):
    isCompleted = models.BooleanField
    numGrade = models.PositiveIntegerField
    student = models.ForeignKey(The_User)