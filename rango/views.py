from django.shortcuts import render

from django.http import HttpResponse

#each view exists within the views.py file as a series of individual functions
#each view takes at least one argument - a HttpRequest object whichalso lives in the django.http module
#Each view must return a HttpResponse object. A simple HttpResponse object takes a string
#parameter representing the content of the page we wish to send to the client requesting the view
def index(request):
    context_dict = { 'boldmessage' : "I am bold font from the context"}
    return render( request, 'rango/index.html', context_dict )
