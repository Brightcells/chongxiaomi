from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'chongxiaomi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^', include('officialsite.urls', namespace='officialsite')),
    # url(r'^api/', include('api.urls', namespace='api')),
    url(r'^data/', include('data.urls', namespace='data')),
)

urlpatterns += staticfiles_urlpatterns('static')

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
