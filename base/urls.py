from django.urls import path, include
from .views import HomePageView, CourseListView, CourseDetailView, SignUp

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('course/', CourseListView.as_view(), name='course_list'),
    path('course/<int:pk>', CourseDetailView.as_view(), name='course_detail'),
    path('signup/', SignUp.as_view(), name='signup'),
  
    
]