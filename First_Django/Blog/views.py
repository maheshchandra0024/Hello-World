from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
hey = [
	{
		"Year" : "2022",
		"Make" : "CHEVY",
		"Model": "DYNAMITE"
	}
]


def Home(request):
	context = {'ke':hey}
	return render(request,'Home.html',context)

