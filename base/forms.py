from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm
from .models import The_User, UserGrade

class The_UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = The_User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'bio',)

class The_UserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = The_User
        fields = UserChangeForm.Meta.fields

class UserGradeForm(ModelForm):
    class Meta:
        model = UserGrade
        fields = ['isCompleted', 'numGrade', 'student', 'course']
