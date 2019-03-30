from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
hey = [
	{
		"Year" : "1906",
		"Make" : "CHEVROLET",
		"Model": "PIMPALA"
	}
]


def Home(request):
	context = {'ke':hey}
	return render(request,'Home.html',context)

