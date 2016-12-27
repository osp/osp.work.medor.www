from django.conf.urls import url
from buy.views import retail_outlet_as_csv


urlpatterns = [
    url(r'^retail-outlets/$', retail_outlet_as_csv, name='retail-outlets-as-csv'),
]
