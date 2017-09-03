from django.conf.urls import url, include
from . import views

urlpatterns = [
	url('^$', views.album, name="album"),
	url(r'^(?P<pk>\d+)/$', views.album_detail, name='album_detail'),
]