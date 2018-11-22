from django.conf.urls import url
from home.views import index, get_about, get_activities_summary, get_documentation

urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^about/', get_about, name="about"),
    url(r'^activities/', get_activities_summary, name="activities"),
    url(r'^documentation/', get_documentation, name="documentation"),
    ]