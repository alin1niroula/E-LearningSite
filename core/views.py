from django.shortcuts import render

# Create your views here.
from django.views import View


class BaseView(View):
    views ={}


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')



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


