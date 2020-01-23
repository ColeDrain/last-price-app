from django.shortcuts import render, redirect
from .forms import AddItemForm, PriceForm
from .models import Product, Price
from django.db.models import Q
from django.db.models import Avg, Max, Min

# Create your views here.
def home(request):
	items = Product.objects.all().annotate(avg_price=Avg('price__price'), max_price=Max('price__price'), min_price=Min('price__price')).order_by('name')
	return render(request, 'index.html', {'items': items})

def search(request):
	query = request.GET.get("q")

	if query is not None and query != '':
		items = Product.objects.filter(Q(name__icontains=query)).annotate(avg_price=Avg('price__price'), max_price=Max('price__price'), min_price=Min('price__price'))
	else:
		return redirect ('home')
	return render(request, 'search.html', {'items': items})

def add(request):
	if request.method == 'POST':
		add_form = AddItemForm(request.POST, request.FILES)
		price_form = PriceForm(request.POST)
		if add_form.is_valid() and price_form.is_valid():
			# Store data from form in variables
			name = add_form.cleaned_data.get('name')
			location = add_form.cleaned_data.get('location')
			image = add_form.cleaned_data.get('image')
			price = price_form.cleaned_data.get('price')
			date_uploaded = price_form.cleaned_data.get('date_uploaded')
			if Product.objects.filter(name=name, location=location).exists():
				item = Product.objects.get(name=name, location=location)
				pr = Price.objects.create(
					price=price,
					date_uploaded=date_uploaded
				)
				item.price.add(pr)
				return redirect('home')
			else:
				pr = Price.objects.create(
					price=price,
					date_uploaded=date_uploaded
				)
				product = Product(
					name=name,
					image=image,
					location=location,
				)
				product.save()
				product.price.add(pr)
				return redirect('home')

	else:
		add_form = AddItemForm()
		price_form = PriceForm()
	return render(request, 'add.html', {'add_form': add_form, 'price_form': price_form})

def about(request):
	return render(request, 'about.html')

def feedback(request):
	return render(request, 'feedback.html')