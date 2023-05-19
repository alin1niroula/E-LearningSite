from django.shortcuts import render
from .models import *
# Create your views here.
from django.views import View


class Base(View):
    views ={}


class IndexView(View):
    def get(self, request):
        views = {}
        views['categories'] = Category.objects.all()
        views['ourstudentsays'] = OurStudentSays.objects.all()
        views['courseCategories'] = CourseCategory.objects.all()
        views['popularcourses'] = PopularCourse.objects.all()
        views['expertinstructors'] = ExpertInstructors.objects.all()
        return render(request, 'index.html', views)



class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

class CoursesView(View):
    def get(self, request):
        # Add your logic here to retrieve course data or perform other actions
        return render(request, 'courses.html')
	


class TeamView(View):
	def get(self,request):
		return render(request, 'team.html')


class AboutView(View):
	def get(self,request):
		return render(request, 'about.html')


class TestimonialView(View):
	def get(self,request):
		return render(request, 'testimonial.html')

class PopularcoursesView(View):
    def get(self, request):
        return render(request, 'popularcourses.html')


