from django.conf.urls import url

from . import views

app_name = 'no'
urlpatterns = [

    url(r'^$', views.index_views, name='index'),
    url(r'^add/$', views.add, name='add'),
]
