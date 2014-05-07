from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from py_sfa.views import *
from iislogs import views as iislogs_views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'py_sfa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    url(r'^test/$', test),
    url(r'^iislogs/list$', iislogs_views.list),
)
