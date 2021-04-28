from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import The_UserCreationForm, The_UserChangeForm
from .models import Course


# Create your views here.


class HomePageView(TemplateView):
    template_name = "home.html"


class CourseListView(ListView):
    model = Course
    template_name = "course_list.html"

class CourseDetailView(DetailView):
    model = Course
    template_name = "course_detail.html"
    context_object_name = "Course"


class SignUp(CreateView):
    form_class = The_UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"

def change_course(request, instruction, pk):
    course = Course.objects.get(pk=pk)
    if instruction == 'subscribe':
        Course.subscribe(request.The_User, course)
    elif instruction == 'unsubscribe':
        Course.unsubscribe(request.The_User, course)
    return redirect('Course:index')