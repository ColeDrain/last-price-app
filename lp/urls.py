from django.urls import path
from lp import views

urlpatterns=[
	path('', views.home, name='home'),
	path('search/', views.search, name='search'),
	path('home/add/', views.add, name='add'),
	path('about/', views.about, name='about'),
	path('feedback/', views.feedback, name='feedback'),
]
