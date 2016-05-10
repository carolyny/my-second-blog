from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$',views.about, name='about'),
    url(r'^about/$', views.about, name='about'),
    url(r'^post/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail')
]
