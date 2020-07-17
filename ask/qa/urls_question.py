from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.void),
	url(r'^(?P<id>[0-9]+)/$', views.question),
]