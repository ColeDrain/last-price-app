from django.db import models

# Create your models here.

class Price(models.Model):
	price = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f'({self.price})'

class Product(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField(upload_to='uploads/')
	location = models.CharField(max_length=200)
	price = models.ManyToManyField(Price)

	def __str__(self):
		return self.name

		