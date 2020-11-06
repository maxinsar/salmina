from django.shortcuts import render, get_object_or_404
from .models import Pages


def page_list(request):
	pages = Pages.objects.all()
	return render(request, 'pages/page_list.html', {'pages':pages})


def page_view(request, slug):
	page = get_object_or_404(Pages, slug=slug)
	return render(request, 'pages/page_view.html', {'page':page})