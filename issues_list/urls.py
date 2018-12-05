from django.conf.urls import url, include
from issues_list.views import get_issues_list, get_issue_detail, create_an_item, edit_an_item, cast_an_upvote, add_comment_to_issue

urlpatterns = [
    url(r'^issues_list/$', get_issues_list, name='issues_list'),
    url(r'^issue_detail/(?P<id>\d+)/$', get_issue_detail, name='issue_detail'),
    url(r'^issues_list/add$', create_an_item, name = 'add'),
    url(r'^issues_list/edit/(?P<id>\d+)/$', edit_an_item, name='edit'),
    url(r'^issues_list/upvote/(?P<id>\d+)/$', cast_an_upvote, name='upvote'),
    url(r'^issue_comment/(?P<id>\d+)/$', add_comment_to_issue, name='issue_comment'),
]