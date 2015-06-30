
from django.conf.urls import url
from first_blog.views import (UserHomePageView, NewEntryView, SignUpPageView, GeneralHomePageView, ListOfBlogEntryViews,
    LoginView)

from . import views

urlpatterns = [
    url(r'^$', GeneralHomePageView.as_view(), name='home_page'),
    url(r'^(?P<user_name>.*)/home/$', UserHomePageView.as_view(), name='user_home_page'),
    url(r'^sign-in/$', SignUpPageView.as_view(), name='sign_up_page'),
    url(r'^/Log-In/$', LoginView.as_view(), name='log_in_page'),
    url(r'^(?P<user_name>.*)/new-blog-entry/$',NewEntryView.as_view(), name='new_blog_entry'),
    url(r'^(?P<user_name>.*)/home/list-of-blog-entries/$', ListOfBlogEntryViews.as_view(), name='list_all_blog_entries')
    ,
]