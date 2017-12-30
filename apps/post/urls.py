from django.conf.urls import url
from .views import home,crear_post_general,list_post_general,detail_post_general
from django.contrib.auth.decorators import login_required

urlpatterns =  [
	url(r'^$',home,name = "index"),
	url(r'^nueva_entrada/general/',login_required(crear_post_general),name = "crear_post_general"),
	url(r'^list/general/',list_post_general,name = "listar_post_general"),
	url(r'^detail/general/(?P<pk>[0-9]+)$',detail_post_general,name = "detail_post_general"),
	
]