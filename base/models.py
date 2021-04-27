from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
# Create your models here.

# user model
class The_User(AbstractUser):

    def __str__(self):
        return self.username

class Course(models.Model):
    title = models.CharField(default=None, max_length=40)
    startDate = models.DateField(default=None)
    endDate = models.DateField(default=None)
    description = models.TextField(default=None, max_length=200)
    students = models.ManyToManyField(The_User, related_name='courses_completed')
    available = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])

    def __str__(self):
        return self.title



# Class/Student elements        
class UserGrade(models.Model):
    isCompleted = models.BooleanField
    numGrade = models.PositiveIntegerField
    student = models.ForeignKey(The_User, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

