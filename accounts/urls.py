from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile
urlpatterns = [
    url(r'^accounts/logout/$', logout, name="logout"),
    url(r'^accounts/login/$', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    ]