from django.conf.urls import patterns, url
from .views import ArticleProposalView, ArticleProposalThanksView, ArticleProposalListView


urlpatterns = patterns('',
    url(r'^$', ArticleProposalView.as_view(), name='article-proposal'),
    url(r'^merci/$', ArticleProposalThanksView.as_view(), name='article-proposal-thanks'),
    url(r'^propositions/$', ArticleProposalListView.as_view(), name='article-proposal-list'),
)
