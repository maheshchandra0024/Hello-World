from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
hey = [
	{
		"Year" : "1111",
		"Make" : "CHEVY",
		"Model": "MALIBU"
	}
]


def Home(request):
	context = {'ke':hey}
	return render(request,'Home.html',context)

