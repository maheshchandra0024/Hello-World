from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
hey = [
	{
		"Year" : "2032",
		"Make" : "CHEVROLET",
		"Model": "PAMPALA"
	}
]


def Home(request):
	context = {'ke':hey}
	return render(request,'Home.html',context)

