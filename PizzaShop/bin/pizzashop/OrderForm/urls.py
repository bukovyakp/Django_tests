#coding:utf8

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'firstapp.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^orders/makeorder/(?P<user_id>\d+)/$', 'OrderForm.views.makeorder'),
                       url(r'^orders/(?P<user_id>\d+)/$', 'OrderForm.views.orders_2'),
                       # url(r'^ajax_test/$', 'OrderForm.views.ajax_test'),
                       url(r'^', 'OrderForm.views.orders'),
                       )
