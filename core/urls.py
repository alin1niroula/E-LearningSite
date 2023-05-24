from .views import *
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('courses/', CoursesView.as_view(), name='courses'),
    path('team/', TeamView.as_view(), name='team'),
    path('about/', AboutView.as_view(), name='about'),
    path('testimonial/', TestimonialView.as_view(), name='testimonial'),
    path('popularcourses/', PopularcoursesView.as_view(), name='popularcourses'),
    
]
