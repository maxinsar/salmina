from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField

class Category(models.Model):
	name = models.CharField(verbose_name = "Название категории", max_length = 220)
	slug = models.SlugField(verbose_name = "URL", max_length = 220)
	images = models.ImageField(upload_to = 'media/category', null = True, blank = True, verbose_name = "Изобржение      ")

	def __str__(self):
		return "{0}".format(self.name)

	def get_absolute_url(self):
		return reverse('blog:category', args = [self.slug])

	class Meta:
		verbose_name = "Категория"
		verbose_name_plural = "Категории"

class ArticleManager(models.Manager):
	def get_queryset(self):
		return super(ArticleManager, self).get_queryset().filter(status = 'published')

class Article(models.Model):
	
	STATUS_CHOICE = (
		('draft', 'Удалить'),
		('published', 'Опубликовать'),
		)

	title = models.CharField(verbose_name = "Заголовок", max_length = 240)
	slug = models.SlugField(verbose_name = "URL", max_length = 240)
	image = models.ImageField(upload_to = 'media/article', verbose_name = "Изображение")
	content = RichTextUploadingField(verbose_name = "Текст", max_length = 10000)
	author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
	published = models.DateTimeField(verbose_name = "Дата публикации", default = timezone.now)
	created = models.DateTimeField(verbose_name = "Дата создания", default = timezone.now)
	updated = models.DateTimeField(verbose_name = "Дата обновления", default = timezone.now)
	category = models.ForeignKey(Category, on_delete = models.CASCADE, verbose_name = "Категория")
	status = models.CharField(verbose_name = "Статус", max_length = 20, choices = STATUS_CHOICE, default = 'published')

	objects = ArticleManager()


	def __str__(self):
		return "Пост - {0}".format(self.title)

	def get_absolute_url(self):
		return reverse('blog:article', args = [
			self.published.year,
			self.published.month,
			self.published.day,
			self.slug]
			)

	class Meta:
		ordering = ('-published',) 
		verbose_name = "Новость"
		verbose_name_plural = "Новости"


class Comments(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
	article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name = "Пост")
	message = models.TextField(max_length = 700, verbose_name = "Сообщение")
	published = models.DateTimeField(verbose_name = "Дата публикации", default = timezone.now)
	active = models.BooleanField(verbose_name = "Активный", default = False)

	def __str__(self):
		return " {0}".format(self.author)

	class Meta:
		verbose_name = "Комментарий"
		verbose_name_plural = "Комментарии"
			