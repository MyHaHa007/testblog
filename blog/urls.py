from django.conf.urls import url
from . import views

app_name = 'blog'
urlpatterns = [
    # 首页
    url(r'^$', views.IndexView.as_view(), name='index'),

    # 博客详情
    url(r'^blog/(?P<pk>[0-9]+)/$', views.detial, name='detail'),

    # 分类-博客
    url(r'^category/(?P<pk>[0-9]+)/$', views.CategoryView.as_view(), name='get_category'),

    # 归档-博客
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives')
]
