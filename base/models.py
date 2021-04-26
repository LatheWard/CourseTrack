from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# user model

class Course(models.Model):
    title = models.TextField
    startDate = models.DateField
    endDate = models.DateField
    description = models.TextField
    size = models.PositiveIntegerField
    avalability = models.PositiveIntegerField

class The_User(AbstractUser):
    coursesCompleted = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.username
        
class UserGrade(models.Model):
    isCompleted = models.BooleanField
    numGrade = models.PositiveIntegerField
    student = models.ForeignKey(The_User, null=True, on_delete=models.SET_NULL)

