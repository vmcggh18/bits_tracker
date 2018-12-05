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
from home.views import index
from home import urls as urls_home
from accounts import urls as urls_accounts
from issues_list import urls as urls_issues_list
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from chart import urls as urls_chart
from blog import urls as urls_blog
from django.views import static
from .settings import MEDIA_ROOT


""" In url patterns define url path, view and name """
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^home/', include(urls_home)),
    url(r'^issues_list/', include(urls_issues_list)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(urls_search)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^chart/', include(urls_chart)),
    url(r'^blog/', include(urls_blog)),
    url(r'^media/(?P<path>.*)$', static.serve,{'document_root': MEDIA_ROOT}),
     
]

