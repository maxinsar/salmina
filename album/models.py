from django.db import models
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField


class Images(models.Model):
	name = models.CharField(verbose_name = "Название", max_length = 224)
	slug = models.SlugField(verbose_name = "URL", max_length = 224)
	image = models.ImageField(upload_to = 'media/', verbose_name = "Изображение")
	description = RichTextUploadingField(verbose_name = "Описание", max_length = 600, blank = True)

	def __str__(self):
		return "Изображение - {0}".format(self.name)

	def get_absolute_url(self):
		return reverse('album', args = [self.slug])

	class Meta:
		verbose_name = "Альбом"
		verbose_name_plural = "Альбомы"


