from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.board, name="board"),
	url(r'^noti_board/$', views.noti_board, name="noti_board"),
	url(r'^info_board/$', views.info_board, name="info_board"),
	url(r'^free_board/$', views.free_board, name="free_board"),
	url(r'^free_board/new/$', views.free_new, name="free_new"),
	url(r'^free_board/(?P<pk>\d+)/$', views.free_detail, name='free_detail'),
	url(r'^free_board/(?P<pk>\d+)/delete$', views.free_delete, name='free_delete'),
	url(r'^free_board/(?P<pk>\d+)/detail$', views.post_detail, name='post_detail'),
	url(r'^free_board/(?P<pk>\d+)/comment/delete$', views.comment_delete, name='comment_delete'),
]
