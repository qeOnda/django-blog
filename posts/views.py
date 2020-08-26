from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.core.paginator import Paginator 

from .models import Post, Category, Client, Comment
from .forms import CommentForm

def search(request):
	queryset = Post.objects.all()
	query = request.GET.get('q')
	if query:
		queryset = queryset.filter(
			Q(title__icontains=query) |
			Q(preview__icontains=query)
		).distinct()
	context = {
		'queryset': queryset,
		'query': query
	}
	return render(request, 'search_result.html', context)	

def index(requests):
	footer = Post.objects.order_by('-time_stamp')[0:2]
	posts = Post.objects.order_by('-id')
	paginator = Paginator(posts, 3)
	page_number = requests.GET.get('page')
	objects = paginator.get_page(page_number)

	return render(requests, 'index.html', {'objects': objects, 'footer': footer})

def about(requests):
	footer = Post.objects.order_by('-time_stamp')[0:2]
	testy = Client.objects.all()
	context = {
		'footer': footer,
		'testy': testy
	}
	return render(requests, 'about.html', context)	

def blog(requests):
	footer = Post.objects.order_by('-time_stamp')[0:2]
	posts = Post.objects.order_by('-id')
	paginator = Paginator(posts, 9)
	page_number = requests.GET.get('page')
	objects = paginator.get_page(page_number)
	return render(requests, 'blog.html', {'footer': footer, 'objects': objects})

def blog_single(requests, id):
	post = Post.objects.get(pk=id)
	category = Category.objects.all()
	footer = Post.objects.order_by('-time_stamp')[0:2]
	recent = Post.objects.order_by('-time_stamp')[0:3]
	if requests.method == 'POST':
		form = CommentForm(requests.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('blog_single', id=post.id)
	else:
		form = CommentForm()
	context = {
		'id': id,
		'form': form,
		'footer': footer,
		'post': post,
		'recent': recent,
		'category': category	
	}

	return render(requests, 'blog-single.html', context)	

def cat(request, slug):
	footer = Post.objects.order_by('-time_stamp')[0:2]
	cats = Post.objects.filter(categories__title=slug)
	cats = cats.order_by('-time_stamp')
	context = {
		'cats': cats,
		'footer': footer,
		'slug': slug
	}
	return render(request, 'cat.html', context)


