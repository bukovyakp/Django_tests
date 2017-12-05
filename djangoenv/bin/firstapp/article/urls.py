#coding:utf8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'firstapp.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^1/', 'article.views.basicone'),
                       url(r'^2/', 'article.views.template_two'),
                       url(r'^3/', 'article.views.template_three_simple'),
                       url(r'^articles/all/$', 'article.views.articles'),
                       url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
                       url(r'^articles/addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
                       url(r'^article/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
                       url(r'^', 'article.views.articles'),
                       )
