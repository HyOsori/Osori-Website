from django.shortcuts import render

# Create your views here.
def album(request):
    return render(request, 'album/album_list.html', {})