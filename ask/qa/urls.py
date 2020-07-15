from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.test),
	url(r'^[0-9]+/$', views.test),
]