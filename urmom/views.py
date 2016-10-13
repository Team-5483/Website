from django.http import HttpResponse
from django.template import loader
from .models import Album


def index(request):
    all_albums = Album.objects.all()
    template = loader.get_template('urmom/index.html')
    context = {
        'all_albums': all_albums
    }
    return HttpResponse(template.render(context, request))


def detail(request, album_id):
    return HttpResponse("<h1> Album id : " + str(album_id) + "</h1>")