__author__ = 'Administrator'
from django.conf.urls import url
import re

from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^(?P<user_name>.*)/home/$', views.user_home_page, name='user_home_page'),
    url(r'^sign-in/$', views.sign_up_page, name='sign_up_page'),
    url(r'^/Log-In/$', views.log_in_page, name='log_in_page'),
    url(r'^(?P<user_name>.*)/new-blog-entry/$', views.new_blog_entry, name='new_blog_entry'),
    url(r'^(?P<user_name>.*)/home/list-of-blog-entries/$', views.list_all_blog_entries, name='list_all_blog_entries'),
]