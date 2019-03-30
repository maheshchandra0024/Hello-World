from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
hey = [
	{
		"Year" : "2012",
		"Make" : "CHEVROLET",
		"Model": "CRUZE"
	}
]


def Home(request):
	context = {'ke':hey}
	return render(request,'Home.html',context)

