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
    template = 'coursedetail.html'

class CourseCreateView(CreateView):
    model = Course
    template = 'course_new.html'
    fields = ['title', 'startDate', 'endDate', 'description', 'size', 'availability']




# Possible Student detail page?

