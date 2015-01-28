from django.conf.urls import patterns, url
from .views import ArticleProposalView, ArticleProposalThanksView


urlpatterns = patterns('',
    url(r'^$', ArticleProposalView.as_view(), name='article-proposal'),
    url(r'^thanks/$', ArticleProposalThanksView.as_view(), name='article-proposal-thanks'),
)
