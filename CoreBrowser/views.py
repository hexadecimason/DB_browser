from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse("Index view.")

def browser_app(request):
	return HttpResponse("Core Browser HTML will be here.")
