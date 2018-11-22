from django.conf.urls import url
from chart.views import charts, chart_bugs, chart_features, chart_issues, get_time_spent

urlpatterns = [
    url(r'^charts/$', charts, name='charts'),
    url(r'^bugs/$', chart_bugs, name='bugs'),
    url(r'^features/$', chart_features, name='features'),
    url(r'^chart_issues/$', chart_issues, name='chart_issues'),
    url(r'^time_spent/$', get_time_spent, name='time_spent'),
    #url(r'^last_week/$', last_week, name='last_week'),
    ]