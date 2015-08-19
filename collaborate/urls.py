from django.conf.urls import patterns, url
from .views import ArticleProposalSimpleView, ArticleProposalView, ArticleProposalThanksView, ArticleProposalListView, ArticleProposalDetailView


urlpatterns = patterns('',
    url(r'^$', ArticleProposalView.as_view(), name='article-proposal'),
    url(r'^simple/$', ArticleProposalSimpleView.as_view(), name='article-proposal-simple'),
    url(r'^merci/$', ArticleProposalThanksView.as_view(), name='article-proposal-thanks'),
    url(r'^propositions/$', ArticleProposalListView.as_view(), name='article-proposal-list'),
    url(r'^propositions/(?P<pk>\d+)/$', ArticleProposalDetailView.as_view(), name='article-proposal-detail'),
)
