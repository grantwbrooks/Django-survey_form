from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^surveys/process/$', views.process),
    url(r'^result/$', views.result),
    # url(r'^surveys/goback/$', views.goback),
    url(r'^surveys/reset/$', views.reset)
]