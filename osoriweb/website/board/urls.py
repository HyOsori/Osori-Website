from django.conf.urls import url, include
from . import views

urlpatterns = [
	url('^$', views.board, name="board"),
	url('^noti_board/', views.noti_board, name="noti_board"),
	url('^info_board/', views.info_board, name="info_board"),
	url('^free_board/', views.free_board, name="free_board"),

]