from django.shortcuts import render, redirect
from .forms import SightingForm
from .models import SightForm, TheoryForm
from .models import Theory, Sighting, BlogPost

def index(request):
	posts = BlogPost.objects.all()
	context = {'posts':posts}
	return render(request, 'pages/index.html', context)

def bpostdetail(request, bpost_slug):
	post = BlogPost.objects.get(slug=bpost_slug)
	context = {'post':post}
	return render(request, 'pages/bpostdetail.html', context)

def intro(request):
	return render(request, 'pages/intro.html')

def introcases(request):
	return render(request, 'pages/introcases.html')

def introtheories(request):
	return render(request, 'pages/introtheories.html')

def braveneworld(request):
	return render(request, 'pages/brave_new_world.html')

def fermi(request):
	return render(request, 'pages/fermi.html')

def sighting(request):
	if request.method == 'POST':
		form = SightingForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect ('pages:thanks')
	else:
		form = SightingForm()
	context = {'form':form}
	return render(request, 'pages/sighting.html', context)

def theory(request):
	if request.method == 'POST':
		form = TheoryForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect ('pages:thanks')
	else:
		form = TheoryForm()
		context = {'form':form} 
	return render(request, 'pages/theory.html', context)

def usertheories(request):
	theories = Theory.objects.filter(status='Visible')
	context = {'theories':theories}
	return render(request, 'pages/usertheories.html', context)

def theorydetail(request, th_id):
	theory = Theory.objects.get(id=th_id)
	context = {'theory': theory}
	return render(request, 'pages/theorydetail.html', context)

def thankyou(request):
	return render(request, 'pages/thankyou.html')

def usersightings(request):
	sightings = Sighting.objects.all()
	context = {'sightings':sightings}
	return render(request, 'pages/sightings.html', context)

def sightdetail(request, st_id):
	sighting = Sighting.objects.get(id=st_id)
	context = {'sighting':sighting}
	return render(request, 'pages/sightingdetail.html', context)
