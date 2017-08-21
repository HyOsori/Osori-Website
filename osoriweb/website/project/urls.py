from django.conf.urls import url, include
from . import views

urlpatterns = [
	url('^$', views.project, name="project"),
	url('^proj_doing/', views.proj_doing, name="proj_doing"),
	url('^proj_done/', views.proj_done, name="proj_done"),
]
