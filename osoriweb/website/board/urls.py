from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', views.board, name="board"),
	url(r'^noti_board/$', views.noti_board, name="noti_board"),
	url(r'^info_board/(?P<pk>\d+)/$', views.info_detail, name='info_detail'),
	url(r'^info_board/new/$', views.info_new, name="info_new"),
	url(r'^info_board/$', views.info_board, name="info_board"),
	url(r'^info_board/(?P<pk>\d+)/edit/$', views.info_edit, name='info_edit'),
	url(r'^info_board/(?P<pk>\d+)/remove/$', views.info_remove, name='info_remove'),
	url(r'^info_comment/(?P<pk>\d+)/remove/$', views.info_comment_remove, name='info_comment_remove'),
	url(r'^info_comment/(?P<pk>\d+)/like/$', views.info_like, name='info_like'),
	url(r'^free_board/$', views.free_board, name="free_board"),
]