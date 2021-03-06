"""Arduino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from django_alexa import views
from alexa_channel import views as aviews

urlpatterns = [
    url(r'^', include('django_alexa.urls')),
    # url(r'^talk/', aviews.talk, name='talksb'),
    url(r'^test/', aviews.test, name='test'),
    url(r'^update/', views.update, name='update'),
    url(r'^mqtt/auth', views.auth, name='auth'),
    url(r'^mqtt/superuser', views.superuser, name='superuser'),
    url(r'^mqtt/acl', views.acl, name='acl'),

    # url(r'^admin/', admin.site.urls),
    # url(r'^$', views.index),
    # url(r'^login/$', views.login),
]
