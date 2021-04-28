from django.contrib import admin
from .models import The_User, course, UserGrade

# Register your models here.
admin.site.register(The_User)
admin.site.register(course)
admin.site.register(UserGrade)
