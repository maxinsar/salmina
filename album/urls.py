from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import list_photo, view_photo

urlpatterns = [
    path('', list_photo, name = "list_photo"),
    path('<slug:slug>', view_photo, name = "album"),
]