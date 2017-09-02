from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.select_articles, name="board"),
    url(r'^(?P<board_name>[\w\-]+)$', views.select_articles, name="board_home"),
    url(r'^(?P<board_name>[\w\-]+)/(?P<page>\d+)$', views.select_articles, name="board_page"),
    url(r'^(?P<board_name>[\w\-]*)/(?P<pk>\d+)/detail$', views.read_article, name='read_article'),
    url(r'^(?P<board_name>[\w\-]*)/new/$', views.create_article, name='create_article'),
    url(r'^(?P<board_name>[\w\-]*)/(?P<pk>\d+)/edit/$', views.edit_article, name='update_article'),
    url(r'^e(?P<board_name>[\w\-]*)/(?P<pk>\d+)/remove/$', views.remove_article, name='delete_article'),
]