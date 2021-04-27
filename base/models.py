from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.


class Course(models.Model):
    title = models.CharField(default=None, max_length=40)
    startDate = models.DateField(default=None)
    endDate = models.DateField(default=None)
    description = models.TextField(default=None, max_length=200)

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

# user model
class The_User(AbstractUser):
    coursesCompleted = models.ManyToManyField(Course, related_name='student')

    def __str__(self):
        return self.username


# Class/Student elements        
class UserGrade(models.Model):
    isCompleted = models.BooleanField
    numGrade = models.PositiveIntegerField
    student = models.ForeignKey(The_User, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

