from django.shortcuts import render, get_object_or_404 
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.db.models import Count
from .models import Article, Category, Comments




def article_list(request):

	articles = Article.objects.all()
	paginator = Paginator(articles, 10)
	page = request.GET.get('page', 1)

	try:
		article = paginator.page(page)
	except PageNotAnInteger:
		article = paginator.page(1)
	except EmptyPage:
		article = paginator.page(paginator.num_pages)

	return render(request, 'blog/post_all.html', {'articles':article})


def article_detail(request, year, month, day, slug):
	article = get_object_or_404(Article, 
		slug = slug,
		status = 'published',
		published__year = year,
		published__month = month,
		published__day = day,

		)
	return render(request, 'blog/detail.html', {'article':article})

def category(request, slug):
	category = get_object_or_404(Category, slug = slug)
	return render(request, 'blog/category.html', {'category':category})