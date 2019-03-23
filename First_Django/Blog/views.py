from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
hey = [
	{
		"Year" : "2012",
		"Make" : "BUICK",
		"Model": "CENTURY"
	}
]


def Home(request):
	context = {'ke':hey}
	return render(request,'Home.html',context)

