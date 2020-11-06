from django.urls import path
from .views import article_list, article_detail, category
from django.contrib.sitemaps.views import sitemap
from blog.sitemap import ArticleSitemap

sitemaps = {
    'articles': ArticleSitemap,
}
app_name = 'blog'

urlpatterns = [
    path('', article_list, name = 'home'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', article_detail, name = 'article'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
         path('category/<slug:slug>', category, name = 'category'),
]
