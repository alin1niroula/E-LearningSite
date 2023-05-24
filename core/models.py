from django.db import models

# Create your models here.


class Category(models.Model):
	name = models.CharField(max_length =400 )
	logo = models.CharField(max_length=300)
	discriptions = models.CharField(max_length = 800)
	slug = models.CharField(max_length=300,unique=True)

	def __str__(self):
		return self.name




class CourseCategory(models.Model):
	name = models.CharField(max_length = 300)
	category = models.ForeignKey(Category,on_delete=models.CASCADE)
	image = models.ImageField(upload_to='media')
	slug = models.CharField(max_length=300,unique=True)
	subcourse = models.CharField(max_length = 300, blank = True,null = True)

	def __str__(self):
		return self.name
        

class PopularCourse(models.Model):
    name = models.CharField(max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    instructor = models.CharField(max_length=100)
    duration = models.FloatField()
    maxstudent = models.IntegerField()
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=300, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

        

class ExpertInstructors(models.Model):
	name = models.CharField(max_length=300)
	image = models.ImageField(upload_to ='media')
	post = models.CharField(max_length= 300)

	def __str__(self):
		return self.name


class OurStudentSays(models.Model):
	name = models.CharField(max_length=300)
	image = models.ImageField(upload_to='media')
	faculty = models.CharField(max_length = 500)
	comment = models.TextField()

	def __str__(self):
		return self.name


class Contact(models.Model):
	name = models.CharField(max_length = 200)
	subject = models.CharField(max_length=400)
	message = models.TextField()

	def __str__(self):
		return self.name

class Gallary(models.Model):
	name = models.CharField(max_length = 200, blank = True)
	image = models.ImageField(upload_to='media')
	url = models.URLField(max_length = 100, blank = True, null = True)
	def __str__(self):
		return str(self.name)

        