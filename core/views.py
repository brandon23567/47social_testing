from django.shortcuts import render

def index(request):
	return render(request, "core/index.html")

def home(request):
	return render(request, "core/home.html")

def privacy_policy(request):
	return render(request, "core/privacy_policy.html")

def terms_of_service(request):
	return render(request, "core/terms_of_service.html")