from django.db import models
from django.urls import reverse




class Product(models.Model):
	name=models.CharField("Наименование",max_length=50)
	picture=models.ImageField(upload_to='img')
	text=models.TextField("Описание",max_length=500)
	healthy=models.ForeignKey('Usefulness', on_delete=models.PROTECT,null=True)
	date=models.DateTimeField("Время",auto_now=True)
	views=models.IntegerField(default=0)
	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("main_page")

	class Meta:
		verbose_name="Продукт"
		verbose_name_plural="Продукты"
		ordering=['name']



class Usefulness(models.Model):
	healthy=models.CharField(max_length=50, db_index=True)

	def __str__(self):
		return self.healthy

	class Meta:
		verbose_name="Полезность"
		verbose_name_plural="Полезности"
		