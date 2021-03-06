from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eDomitory.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','manager.views.index', name='index'),
    url(r'^login/','manager.views.login', name='login'),
    url(r'^logout/','manager.views.logout', name='logout'),
    url(r'^switch/','manager.views.switch', name='switch'),
    url(r'^sensor/','manager.views.sensor', name='sensor'),
    url(r'^settings/','manager.views.settings', name='settings'),
    url(r'^api/server/login/','api.server.views.login', name='login_server'),
    url(r'^api/server/switchUpdate/','api.server.views.switchUpdate', name='switchUpdate'),
    url(r'^api/client/notify/','api.client.views.notify', name='notify'),

)
