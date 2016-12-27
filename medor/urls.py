from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from cms.sitemaps import CMSSitemap
from django.contrib.sitemaps.views import sitemap


admin.autodiscover() # Not required for Django 1.7.x+


urlpatterns = [
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),
]


urlpatterns = i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^filer/', include('filer.urls')),
    url(r'^subscribe/', include('subscribe.urls')),
    url(r'^buy/', include('buy.urls')),
    url(r'^', include('publish.urls')),
    url(r'^', include('cms.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
