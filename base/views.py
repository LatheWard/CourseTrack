from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from .forms import The_UserCreationForm, The_UserChangeForm, UserGradeForm
from .models import course, The_User


# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class CourseListView(ListView):
    model = course
    template_name = "course_list.html"

class CourseDetailView(LoginRequiredMixin, DetailView):
    model = course
    template_name = "course_detail.html"
    context_object_name = "course"

class UserDetailView(LoginRequiredMixin, DetailView):
    model = The_User
    template_name = "user_detail.html"
    context_object_name = "user_profile"

class SignUp(CreateView):
    form_class = The_UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

def get_user_profile(request):
    return render(request, 'user_detail.html')

def change_course(request, instruction, pk):
    tCourse = course.objects.get(pk=pk)
    if instruction == 'subscribe':
        course.subscribe(request.user, tCourse)
    elif instruction == 'unsubscribe':
        course.unsubscribe(request.user, tCourse)
    return redirect('course_list')

class UserGradeFormView(CreateView):
    form_class = UserGradeForm
    success_url = reverse_lazy("home")
    template_name = "course_complete.html"
