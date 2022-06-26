from django.shortcuts import render, redirect, get_object_or_404
from . import views
from .models import UserBlogPost, UserBlogPostForm

def index(request):
	posts = UserBlogPost.objects.all()
	context = {'posts':posts}
	return render(request, 'blog/index.html', context)

def submitarticle(request):
	if request.method == 'POST':
		form = UserBlogPostForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect ('pages:thanks')
	else:
		form = UserBlogPostForm()
		context = {'form':form}
	return render(request, 'blog/submitarticle.html', context)

def userpostdetail(request, year, month, day, slug):
	post = get_object_or_404(UserBlogPost,
							 status='published',
							 published__year=year,
							 published__month=month,
							 published__day=day,
							 slug=slug)

	context = {'post': post}
	return render(request, 'blog/userpostdetail.html', context)


