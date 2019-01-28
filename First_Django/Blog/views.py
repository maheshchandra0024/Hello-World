from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
hey = [
	{
		"Year" : "2004",
		"Make" : "HONDA",
		"Model": "ACCORD COUPE"
	}
]
def Home(request):

	context = {'k':hey}
	return render(request,'Home.html',context)

