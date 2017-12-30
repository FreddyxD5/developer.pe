"""openyourmind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import login,logout_then_login
from apps.post.views import home
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',home,name = "index"),
    url(r'^post/',include('apps.post.urls', namespace = "post")),
    url(r'^accounts/login', login,{'template_name':'usuarios/login2.html'},name='login'),
 	url(r'^logout/',logout_then_login,name='logout'),
    url(r'^tinymce/', include('tinymce.urls')),
    #url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


