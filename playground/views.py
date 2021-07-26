from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def say_hello(request):
    return render(request, 'hello.html', {'name': 'People'})


# request -> response


# request handler


# action
