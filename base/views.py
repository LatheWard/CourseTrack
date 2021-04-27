from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView
from .models import Course
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class CourseListView(ListView):
    model = Course
    template_name = 'course_list.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'course_detail.html'

# Possible Student detail page?

