from django.db import models
from django.conf import settings
from django.urls import reverse
from django.forms import ModelForm
from django.contrib.auth import get_user_model

VISIBILITY = [
			('Visible', 'Visible'),
			('Hidden', 'Hidden'),
]

class Sighting(models.Model):
	subj = models.CharField(max_length=100)
	body = models.TextField()
	location = models.CharField(max_length=100)
	added = models.DateTimeField(auto_now_add=True)
	time_of = models.CharField(max_length=100)
	name = models.CharField(max_length=80, blank=True, null=True)

	def __str__(self):
		return self.subj

class SightForm(ModelForm):
	class Meta:
		model = Sighting
		fields = ['subj', 'body', 'location', 'time_of']

class Theory(models.Model):

	VISBILITY = (
		('visible', 'Visible'),
		('hidden', 'hidden'),)

	theory_area = (
		('1', 'UFO/UAPs nature'),
		('2', 'Origins of UFO/Aliens'),
		('3', 'Where they come from'),
		('4', 'Their intentions'),
		('5', 'Other'),)


	Title = models.CharField(max_length=100)
	Subject = models.CharField(max_length=10,
							   choices=theory_area)
	Details = models.TextField()
	Name = models.CharField(max_length=100, blank=True, null=True)
	added = models.DateTimeField(auto_now_add=True)
	status = models.CharField(max_length=20,
							  choices=VISIBILITY,
							  default='hidden')
	email = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return self.Title

class TheoryForm(ModelForm):
	class Meta:
		model = Theory
		fields = ['Title', 'Subject', 'Details', 'Name', 'email',]
		labels = {"Title": "Title",
				  "Name": "Name (optional)",
				  "email": "Email (optional)",
		}

class BlogPost(models.Model):
	title = models.CharField(max_length=100)
	body = models.TextField()
	author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
	added = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(max_length=100, unique=True)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse ('pages:bpostdetail', args=[self.slug])

	def save(self, *args, **kwargs):
		self.slug = self.slug or slugify(self.title)
		super().save(*args, **kwargs)