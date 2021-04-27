from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView
from .models import Course
# Create your views here.

class HomePageView(TemplateView):
    basepage = 'base.html'

class HomePageView(TemplateView):
    homepage = 'home.html'

class CourseListView(ListView):
    model = Course
    template = 'course_list.html'

class CourseDetailView(DetailView):
    model = Course
    template = 'course_detail.html'






# Possible Student detail page?

