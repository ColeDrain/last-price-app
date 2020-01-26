from django.shortcuts import render, redirect
from .forms import AddItemForm, PriceForm, FeedbackForm
from .models import Product, Price
from django.db.models import Q
from django.db.models import Avg, Max, Min
from lastprice.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.template.loader import get_template
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
			#image = add_form.cleaned_data.get('image')
			price = price_form.cleaned_data.get('price')
			if Product.objects.filter(name=name, location=location).exists():
				item = Product.objects.get(name=name, location=location)
				pr = Price.objects.create(
					price=price
				)
				item.price.add(pr)
				return redirect('home')
			else:
				pr = Price.objects.create(
					price=price
				)
				product = Product(
					name=name,
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
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			user_email = form.cleaned_data.get('email')
			message = form.cleaned_data.get('message')

			template = get_template('feedback_template.txt') 
			context = {
				'name': name,
				'email': user_email,
				'message': message,
			}

			content = template.render(context)
			email = EmailMessage(
				"New contact form submission (LastPrice.ng)",
				content,
				user_email,
				[EMAIL_HOST_USER],
				headers = {'Reply-To': user_email},
				)
			email.send()
			request.session['mail_sent'] = True
			return redirect ('success')
	else:
		form = FeedbackForm()	
	return render(request, 'feedback.html', {'form':form})

def success(request):
	if not request.session.pop('mail_sent', False):
		return redirect('home')
	else:
		return render(request, 'success.html')