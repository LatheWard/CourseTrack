from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Course(models.Model):
    title = models.TextField
    startDate = models.DateField
    endDate = models.DateField
    description = models.TextField
    size = models.PositiveIntegerField
    avalability = models.PositiveIntegerField

# user model
class The_User(AbstractUser):
    coursesCompleted = models.ManyToManyField(Course, null=True, related_name='student')

    def __str__(self):
        return self.username


# Class/Student elements        
class UserGrade(models.Model):
    isCompleted = models.BooleanField
    numGrade = models.PositiveIntegerField
    student = models.ForeignKey(The_User, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

