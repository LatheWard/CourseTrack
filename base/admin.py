from django.contrib import admin
from .models import Course, The_User, UserGrade

# Register your models here.
admin.site.register(Course)
admin.site.register(UserGrade)