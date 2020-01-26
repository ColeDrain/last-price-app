from django import forms
from .models import Product, Price

class AddItemForm(forms.ModelForm):
	
	class Meta:
		model = Product
		fields = ('name','location',)

class PriceForm(forms.ModelForm):

	class Meta:
		model = Price
		fields = ('price',)

class FeedbackForm(forms.Form):
	name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	message = forms.CharField(required=True, widget=forms.Textarea)