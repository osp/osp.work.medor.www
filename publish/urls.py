from django.conf.urls import url, include
from django.views.generic.base import RedirectView


from rest_framework import routers


from .views import ArticleMembershipWebListView, ArticleListView, ArticleDetailView, IssueListView, IssueDetailView
from .views import RubricViewSet, LicenseViewSet, IssueViewSet, ArticleViewSet, ContributorViewSet, ContributionViewSet, RoleViewSet, ArticleMembershipViewSet


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'rubric', RubricViewSet)
router.register(r'license', LicenseViewSet)
router.register(r'issue', IssueViewSet)
router.register(r'article', ArticleViewSet)
router.register(r'contributor', ContributorViewSet)
router.register(r'role', RoleViewSet)
router.register(r'contribution', ContributionViewSet)
router.register(r'article-membership', ArticleMembershipViewSet)


urlpatterns = [
    url(r'^$', ArticleMembershipWebListView.as_view(), name='feed'),

    url(r'^numero/$', IssueListView.as_view(), name='issue-list'),
    url(r'^numero/(?P<slug>[-\w]+)/$', IssueDetailView.as_view(), name='issue-detail-site'),

    url(r'^article/$', ArticleListView.as_view(), name='article-list'),
    url(r'^article/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail-site'),

    # legacy urls
    url(r'^bug/$', RedirectView.as_view(url='/article/le-jour-ou-la-belgique-bugge/', permanent=True)),
    url(r'^ag-2015/$', RedirectView.as_view(url='/article/ag-2015/', permanent=True)),
    url(r'^en-attendant-medor/2015/06/09/instruction-judiciaire-francois-fornieri-mithra/$', RedirectView.as_view(url='/article/instruction-judiciaire-ouverte-contre-francois-fornieri-et-mithra/', permanent=True)),
    url(r'^en-attendant-medor/2015/11/17/vie-privee-stib/$', RedirectView.as_view(url='/article/le-silence-du-tram/', permanent=True)),
    url(r'^en-attendant-medor/\d\d\d\d/\d\d/\d\d/(?P<slug>[-\w]+)/$', RedirectView.as_view(pattern_name='article-detail-site', permanent=True)),

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
