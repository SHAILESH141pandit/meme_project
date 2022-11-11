from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return HttpResponse("<h1>Welcome to Meme app.")


def register(request):
    return render(request, "Register.html")
