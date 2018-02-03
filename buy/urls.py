from django.conf.urls import url
from buy.views import retail_outlet_as_csv, article_27_as_csv


urlpatterns = [
    url(r'^retail-outlets/$', retail_outlet_as_csv, name='retail-outlets-as-csv'),
    url(r'^article-27/$', article_27_as_csv, name='article-27-as-csv'),
]
