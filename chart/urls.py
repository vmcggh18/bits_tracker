from django.conf.urls import url
from chart.views import charts, chart_bugs, chart_features

urlpatterns = [
    url(r'^charts/$', charts, name='charts'),
    url(r'^bugs/$', chart_bugs, name='bugs'),
     url(r'^features/$', chart_features, name='features'),

    ]