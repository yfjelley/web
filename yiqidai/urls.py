from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

from bbs import forum
import bbs
from yiqidai import settings


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yiqidai.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^bbs/', include('bbs.forum.urls')),
    url(r'^user/', include('bbs.account.urls')),
    url(r'^search/', include('searcher.urls')),
    url(r'^api/forum/', include(bbs.forum.urls.api_urlpatterns)),
    url(r'^panel/', include('bbs.panel.urls', namespace='panel', app_name='panel')),
    url(r'', include('searcher.urls')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
