from sys import exception
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Well, Box
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def index(request):
	context = {}
	return render(request, "CoreBrowser/index.html", context)

def browser_app(request):
	return HttpResponse("Core Browser HTML will be loaded here.")

def search(request):#, search_type, search_term):

	search_type = request.GET.get('search_type')
	search_term = request.GET.get('search_term')

	match(search_type):
		case "API":
			try:
				well_result = Well.objects.filter(api=search_term)
			except Exception as e:
				return render(request, "CoreBrowser/search_error.html", {"e" : e})
		case "FILE":
			try:
				well_result = Well.objects.filter(file_num=search_term)
			except Exception as e:
				return render(request, "CoreBrowser/search_error.html", {"e" : e})
		case "LEASE":
			try:
				well_result = Well.objects.filter(lease__contains=search_term)
			except Exception as e:
				return render(request, "CoreBrowser/search_error.html", {"e" : e})
		case "FORMATION":
			try:
				well_result = Well.objects.filter(formation__contains=search_term)
			except Exception as e:
				return render(request, "CoreBrowser/search_error.html", {"e" : e})
		case _:
			return render(request, "CoreBrowser/search_error.html", {"e" : "invalid search type"})


	if(len(well_result) == 0):
		return render(request, "CoreBrowser/search_noresults.html", {})

	resultlist = []

	for w in well_result:
		bx = Box.objects.filter(file_num=w.file_num)
		resultlist.append([w, bx])

	context = {"resultlist" : resultlist}

	return render(request, "CoreBrowser/search.html", context)

#def search_error(request):
#	context = {}
#	return render(request, "CoreBrowser/search_error.html", context)
