from django.conf.urls import include, url

from . import views

urlpatterns = [
	url(r'^$', views.new),
	url(r'^[0-9]+/$', views.test),
	url(r'^login/', include('qa.urls_login')),
	url(r'^signup/', include('qa.urls_signup')),
	url(r'^question/', include('qa.urls_question')),
	url(r'^ask/', include('qa.urls_ask')),
	url(r'^popular/', include('qa.urls_popular')),
	url(r'^new/', include('qa.urls_new')),
]