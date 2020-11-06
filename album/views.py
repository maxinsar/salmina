from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Images


def list_photo(request):
	photos = Images.objects.all()
	paginator = Paginator(photos, 10)
	page = request.GET.get('page', 1)

	try:
		photo = paginator.page(page)
	except PageNotAnInteger:
		photo = paginator.page(1)
	except EmptyPage:
		photo = paginator.page(paginator.num_pages)
	return render(request, 'album/list_photo.html', {'photos':photo})


def view_photo(request, slug):
	photo = get_object_or_404(Images, slug=slug)
	return render(request, 'album/view_photo.html', {'photo':photo})
