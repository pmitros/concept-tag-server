from django.conf.urls import patterns, include, url
from wiki.urls import get_pattern as get_wiki_pattern
from django_notify.urls import get_pattern as get_notify_pattern

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^notify/', get_notify_pattern()),
    (r'', get_wiki_pattern()),
    (r'^sample',"conceptajax.views.sample"),
    (r'^get_concept_list',"conceptajax.views.get_concept_list"),
    (r'^get_concept/(\w+)',"conceptajax.views.get_concept"),
    # Examples:
    # url(r'^$', 'conceptserver.views.home', name='home'),
    # url(r'^conceptserver/', include('conceptserver.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
