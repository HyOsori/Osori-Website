from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index_page'),
    url(r'^board/', include('website.board.urls')),
    url(r'^album/', include('website.album.urls')),
    url(r'^project/', include('website.project.urls')),
    url(r'^about/$', views.about, name='about'),
    url(r'^about/history', views.about_history, name='about_history'),
 	url(r'^about/location', views.about_location, name='about_location'),
 	url(r'^about/introduce', views.about_introduce, name='about_introduce'),
    url(r'^contact/$', views.contact, name='contact'),
]