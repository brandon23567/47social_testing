from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('home/', views.home, name="home"),
	path('privacy_policy/', views.privacy_policy, name="privacy_policy"),
	path('terms_of_service/', views.terms_of_service, name="terms_of_service"),
]