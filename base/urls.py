from django.urls import path, include
from .views import HomePageView, CourseListView, CourseDetailView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('course/', CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    
]