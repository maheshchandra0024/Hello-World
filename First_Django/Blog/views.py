from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
hey = [
	{
		"Year" : "2018",
		"Make" : "CHEVROLET",
		"Model": "DOMPALA"
	}
]


def Home(request):
	context = {'ke':hey}
	return render(request,'Home.html',context)

