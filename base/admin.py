from django.contrib import admin
from .models import The_User, Course, UserGrade

# Register your models here.
admin.site.register(The_User)
admin.site.register(Course)
admin.site.register(UserGrade)
