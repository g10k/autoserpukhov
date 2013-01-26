from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from views import index, guess_button

from autorepair.views import autorepair as autorepair_view
from autorepair.views import list,defects,defect_causes,defects_causes_popup

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$',index,name='index'),
    #url(r'^repairs/(?P<id>\d+)/$',autorepair_view, name='autorepair'),
    #url(r'^repairs/$',list,name='repairs'),
    url(r'^places/',include("autocenter.urls")),
    url(r'^',include('autorepair.urls')),
    url(r'^defects/$',defects),
    url(r'^defects/causes/$',defect_causes),
    url(r'^defects/causes_popup/$',defects_causes_popup,name="causes_popup"),
    url(r'^comments/', include('django.contrib.comments.urls')),
    url(r'^play/$',guess_button,name='guess_button'),
    # url(r'^$', 'repairit.views.home', name='home'),
    # url(r'^repairit/', include('repairit.foo.urls')),

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
