from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from cms.sitemaps import CMSSitemap


admin.autodiscover() # Not required for Django 1.7.x+


urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),
    url(r'^subscribe/', include('subscribe.urls')),
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^', include('cms.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
