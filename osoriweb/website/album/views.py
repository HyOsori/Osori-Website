from django.shortcuts import render, get_object_or_404
from .models import Photo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.


def album(request):
    photo_list = Photo.objects.order_by('created_date')
    paginator = Paginator(photo_list, 20)

    page = request.GET.get('page')
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    return render(request, 'album/album_list.html', {'photos': photos})


def album_detail(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    return render(request, 'album/album_detail.html', {'photo': photo})