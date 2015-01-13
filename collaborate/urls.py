from django.conf.urls import patterns, url
from .views import ArticleProposalView


urlpatterns = patterns('',
    url(r'^$', ArticleProposalView.as_view(), name='article-proposal'),
)
