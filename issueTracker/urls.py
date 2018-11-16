"""issueTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from accounts.views import index,  get_about, get_activities_summary
from issues_list.views import get_issues_list, get_issue_detail, create_an_item, edit_an_item, cast_an_upvote, add_comment_to_issue, get_feature_detail
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from chart import urls as urls_chart
from django.views import static
#from .settings import MEDIA_ROOT
#from cart.views import add_to_cart

""" In url patterns define url path, view and name """
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^about/', get_about, name="about"),
    url(r'^activities/', get_activities_summary, name="activities"),
    #URLS RELATING TO ISSUES_LIST APP
    url(r'^issues_list/$', get_issues_list, name='issues_list'),
    url(r'^issue_detail/(?P<id>\d+)/$', get_issue_detail, name='issue_detail'),
    url(r'^issues_list/add$', create_an_item, name = 'add'),
    url(r'^issues_list/edit/(?P<id>\d+)/$', edit_an_item, name='edit'),
    url(r'^issues_list/upvote/(?P<id>\d+)/$', cast_an_upvote, name='upvote'),
    url(r'^issue_comment/(?P<id>\d+)/$', add_comment_to_issue, name='issue_comment'),
    url(r'^feature_detail/(?P<id>\d+)/$', get_feature_detail, name='feature_detail'),
     #URLS RELATING TO CART APP
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^chart/', include(urls_chart)),
    #url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
     
]

