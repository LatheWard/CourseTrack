from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.core.validators import MaxValueValidator

# Create your models here.

# user model
class The_User(AbstractUser):
    bio = models.TextField(default=None, null=True, blank=True)

    def __str__(self):
        return self.username

class course(models.Model):
    title = models.CharField(default=None, max_length=40)
    startDate = models.DateField(default=None)
    endDate = models.DateField(default=None)
    description = models.TextField(default=None, max_length=200)
    students = models.ManyToManyField(The_User, related_name='courses_completed', blank=True, null=True)
    available = models.BooleanField(default=True)

    @classmethod
    def subscribe(cls, current_user, new_course):
        new_course.students.add(current_user)

    @classmethod
    def unsubscribe(cls, current_user, cancel_course):
        cancel_course.students.remove(current_user)

    def get_absolute_url(self):
        return reverse('course_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

# Class/Student elements        
class UserGrade(models.Model):
    isCompleted = models.BooleanField(default=True)
    numGrade = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    student = models.ForeignKey(The_User, null=True, on_delete=models.SET_NULL)
    course = models.ForeignKey(course, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return '{0}, {1}'.format(self.student, self.course)

