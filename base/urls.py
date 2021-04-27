from django.urls import path, include
from .views import HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('course/', HomePageView.as_view(), name='course_list'),
    path('course/[int:pk]', HomePageView.as_view(), name='course_detail'),
    
]