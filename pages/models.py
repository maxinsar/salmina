from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField

class Pages(models.Model):
	name = models.CharField(verbose_name = "Название страницы", max_length = 100)
	slug = models.SlugField(verbose_name = "URL", max_length = 100)
	description = models.CharField(verbose_name = "Описание страницы", max_length = 200)
	keywords = models.CharField(verbose_name = "Ключевые слова", max_length = 240)
	content = RichTextUploadingField(verbose_name = "Контент", max_length = 2400, blank = True)

	def __str__(self):
		return "Страница - {0} ".format(self.name)

	def get_absolute_url(self):
		return reverse('pages:page', args = [self.slug])

	class Meta:
		verbose_name = "Страница"
		verbose_name_plural = "Страницы"
