from django.conf.urls import patterns, include, url
from core.views import UserListView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'core.views.home', name='home'),
    url(r'^login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^users/$', UserListView.as_view(), name='users_list'),
    url(r'^users/(?P<user_id>\d+)/$', 'core.views.edit_user', name='edit_user'),
    url(r'^admin/', include(admin.site.urls), name='admin'),
)
