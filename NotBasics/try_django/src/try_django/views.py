from django.http import HttpResponse

def home_page(request):
	return HttpResponse("hello world")

def about_page(request):
	return HttpResponse("About page")

def contact_page(request):
	return HttpResponse("Contact page")