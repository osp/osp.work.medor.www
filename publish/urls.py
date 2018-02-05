from django.conf.urls import url, include
from django.views.generic.base import RedirectView


from rest_framework import routers


from .views import ArticleMembershipWebListView, ArticleListView, ArticleDetailView, IssueListView, IssueDetailView, ContributorListView, ContributorDetailView
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

    url(r'^contributeurs/$', ContributorListView.as_view(), name='contributor-list'),
    url(r'^contributeurs/(?P<pk>\d+)/$', ContributorDetailView.as_view(), name='contributor-detail'),

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
