from django.conf.urls import patterns, url
from buy.views import retail_outlet_as_csv


urlpatterns = patterns('',
    url(r'^retail-outlets/$', retail_outlet_as_csv, name='retail-outlets-as-csv'),
)
