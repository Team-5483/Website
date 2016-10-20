from django.shortcuts import render
from urmom.models import Album

# Create your views here.
def index(request):
    return render(request, "Home/index.html")

