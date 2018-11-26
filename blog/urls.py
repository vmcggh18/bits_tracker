from django.conf.urls import url
from .views import get_posts, post_detail, create_a_post, edit_a_post, add_comment_to_post

urlpatterns = [
    url(r'^$', get_posts, name='get_posts'),
    url(r'^(?P<pk>\d+)/$', post_detail, name='post_detail'),
    url(r'^new/$', create_a_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', edit_a_post, name='edit_post'),
    url(r'^post_comment/(?P<pk>\d+)/$', add_comment_to_post, name='post_comment'),
    ]