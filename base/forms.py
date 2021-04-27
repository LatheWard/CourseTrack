from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import The_User

class The_UserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = The_User
        fields = UserCreationForm.Meta.fields

class ChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = The_User
        fields = UserChangeForm.Meta.fields


