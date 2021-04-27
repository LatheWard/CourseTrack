from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView
from .models import Course
# Create your views here.

class HomePageView(TemplateView):
    basepage = 'base.html'

class HomePageView(TemplateView):
    homepage = 'home.html'

class CourseDetailView(DetailView):
    model = Course