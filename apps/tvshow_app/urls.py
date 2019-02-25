
from django.conf.urls import url
from . import views
                        
urlpatterns = [
    url(r'^shows/new$', views.index),
    url(r'^shows$', views.index3),
    url(r'^show/create$', views.create),
    url(r'^shows/(?P<id>\d+)$', views.info),
    url(r'^shows/(?P<id>\d+)/edit$', views.edit),
    url(r'^shows/(?P<id>\d+)/destroy$', views.delete),
    url(r'^shows/(?P<id>\d+)/save$', views.save_edit),

]
