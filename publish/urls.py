from django.conf.urls import patterns, url, include
from rest_framework import serializers, viewsets, routers
from .views import IssueListView, ArticleMembershipDetailView, ArticleMembershipDetailRawView, ArticleMembershipDetailCSSView, ArticleMembershipDetailTplView
from .models import Article, ArticleMembership, Issue
from rest_framework import filters, permissions


# Serializers define the API representation.
class IssueSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Issue


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Article


class ArticleMembershipSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = ArticleMembership
        depth = 1


# ViewSets define the view behavior.
class IssueViewSet(viewsets.ModelViewSet):
    queryset = Issue.objects.all()
    serializer_class = IssueSerializer
    permission_classes = (permissions.IsAdminUser,)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (permissions.IsAdminUser,)


class ArticleMembershipViewSet(viewsets.ModelViewSet):
    queryset = ArticleMembership.objects.all()
    serializer_class = ArticleMembershipSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('issue', 'issue__id')
    permission_classes = (permissions.IsAdminUser,)


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'issue', IssueViewSet)
router.register(r'article', ArticleViewSet)
router.register(r'article-membership', ArticleMembershipViewSet)


urlpatterns = patterns('',
    url(r'^$', IssueListView.as_view(), name='issue-list'),
    url(r'^(?P<pk>\d+)/$', ArticleMembershipDetailView.as_view(), name='article-membership-detail'),
    url(r'^(?P<pk>\d+).html$', ArticleMembershipDetailRawView.as_view(), name='article-membership-detail-html'),
    url(r'^(?P<pk>\d+).css$', ArticleMembershipDetailCSSView.as_view(), name='article-membership-detail-css'),
    url(r'^(?P<pk>\d+).tpl$', ArticleMembershipDetailTplView.as_view(), name='article-membership-detail-tpl'),

    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
