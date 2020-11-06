from django.contrib import admin
from .models import Article, Category, Comments


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'published',   
                       'status')
    list_filter = ('status', 'created', 'published', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'published'
    ordering = ('status', 'published')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin): 
    list_display = ('name', 'slug',)  
    search_fields = ('name',)
    prepopulated_fields = {'slug':('name',)}


@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
	list_display = ('author', 'article', 'published', 'active',)
	search_fields = ('article',)
