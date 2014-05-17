from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from iislogs import views

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'py_sfa.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       #url(r'^admin/', include(admin.site.urls)),

                      (r'^iislogs/list$', 'iislogs.views.list'),
                      (r'^iislogs/listhitstats$',
                       'iislogs.views.listhitstats'),
                       )
