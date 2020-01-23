from django import forms
from .models import Product, Price

class AddItemForm(forms.ModelForm):
	
	class Meta:
		model = Product
		fields = ('name', 'image', 'location',)

class PriceForm(forms.ModelForm):

	class Meta:
		model = Price
		fields = ('price',)