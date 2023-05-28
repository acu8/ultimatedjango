from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# request → response
# request handler 

def say_hello(request):
    #Pull data from db
    #Transform, Send email etc.
    return render (request, 'hello.html')
