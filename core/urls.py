from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from views import index, guess_button, search_by_name


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index, name='index'),
    url(r'^search_autocenter_by_name$', search_by_name),
    url(r'^places/', include("autocenter.urls")),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^play/$', guess_button,name='guess_button'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^loginza/', include('loginza.urls')),
     url(r'^users/', include('users.urls')),
     url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )


#from django.conf.urls.static import static
#urlpatterns += static('static',view='django.contrib.staticfiles.views.serve',show_indexes=True)
