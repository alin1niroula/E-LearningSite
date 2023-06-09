from django.shortcuts import render, redirect
from .models import *
from .forms import EnrolForm
# Create your views here.
from django.views import View
from django.utils.datastructures import MultiValueDictKeyError


class Base(View):
    views ={}


class IndexView(View):
    def get(self, request):
        views = {}
        views['categories'] = Category.objects.all()
        views['ourstudentsays'] = OurStudentSays.objects.all()
        views['courseCategories'] = CourseCategory.objects.all()
        views['popularcourses'] = PopularCourse.objects.all()
        views['expertInstructors'] = ExpertInstructors.objects.all()
        views['gallary'] = Gallary.objects.all()
        views['sliders'] = Slider.objects.all
        return render(request, 'index.html', views)




def contact(request):
    views = {}
    views['informations'] = Information.objects.all()
    views['gallary'] = Gallary.objects.all()

    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            subject = request.POST['subject']
            message = request.POST['message']
        except MultiValueDictKeyError:
            views['error_message'] = "Success!"
            return render(request, 'contact.html', views)

        data = Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        views['success_message'] = "Success!"
        return render(request, 'contact.html', views)

    return render(request, 'contact.html', views)



class CoursesView(View):
    def get(self, request):
    	views = {}
    	views['categories'] = Category.objects.all()
    	views['popularcourses'] = PopularCourse.objects.all()
    	views['ourstudentsays'] = OurStudentSays.objects.all()

    	return render(request, 'courses.html', views)
	


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


class EnrolView(View):
    def get(self, request):
        form = EnrolForm()
        return render(request, 'enrol.html', {'form': form})

    def post(self, request):
        form = EnrolForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('enrol_success')
        return render(request, 'enrol.html', {'form': form})

def enrol_success(request):
    return render(request, 'enrol_success.html')