import controllers.mangasusu as mangasusu
from django.urls import path
from django.shortcuts import render
from config import MANGASUSU_BASEURL
def index(request):
    mangas = mangasusu.home(request)
    print(MANGASUSU_BASEURL)
    return render(request, 'mangasusu/index.html', {'body': mangas})

urlpatterns = [
    path('', index, name='index'),
]
