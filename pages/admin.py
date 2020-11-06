from django.contrib import admin

from .models import Pages



@admin.register(Pages)
class PagesAdmin(admin.ModelAdmin):
	list_display = ('name', 'slug', 'keywords')
	prepopulated_fields = {'slug':('name',)}
