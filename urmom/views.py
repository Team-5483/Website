from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from .models import Album

def index(request):
    all_albums = Album.objects.all()
    context = {
        'all_albums': all_albums
    }
    return render(request, "urmom/index.html", context)


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("THERE ARE NO THINGS HERE")

    return render(request, "urmom/detail.html", {'album': album})
