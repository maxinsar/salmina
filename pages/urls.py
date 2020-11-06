from django.urls import path
from .views import page_list, page_view


app_name = "page"
urlpatterns = [
    path('', page_list, name = 'page_list'),
    path('<slug:slug>/', page_view, name = 'page')
]
