from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
hey = [
	{
		"Year" : "2122",
		"Make" : "CHEVY",
		"Model": "PIGLET"
	}
]


def Home(request):
	context = {'ke':hey}
	return render(request,'Home.html',context)

