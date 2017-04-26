from django.conf.urls import url, include
from django.views.generic.base import RedirectView

from rest_framework import serializers, viewsets, routers
from .views import ArticleMembershipWebListView, ArticleDetailView, IssueListView, IssueDetailView, ArticleMembershipDetailView, ArticleMembershipDetailRawView, ArticleMembershipDetailCSSView, ArticleMembershipDetailTplView
from .models import Article, ArticleMembership, Issue, License, Rubric
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend


# Serializers define the API representation.
class RubricSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Rubric
        fields = '__all__'


# Serializers define the API representation.
class LicenseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Issue
        fields = '__all__'


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    rubric = RubricSerializer(required=False)

    class Meta:
        model = Article
        exclude = ('override_image',)


class ArticleMembershipSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    article = ArticleSerializer()

    class Meta:
        model = ArticleMembership
        depth = 1
        fields = '__all__'


# Serializers define the API representation.
class IssueSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    articlemembership_set = ArticleMembershipSerializer(many=True)

    class Meta:
        model = Issue
        fields = '__all__'


# ViewSets define the view behavior.
class RubricViewSet(viewsets.ModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer
    permission_classes = (permissions.IsAdminUser,)


# ViewSets define the view behavior.
class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    permission_classes = (permissions.IsAdminUser,)


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
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('issue', 'issue__id')
    permission_classes = (permissions.IsAdminUser,)


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'rubric', RubricViewSet)
router.register(r'license', LicenseViewSet)
router.register(r'issue', IssueViewSet)
router.register(r'article', ArticleViewSet)
router.register(r'article-membership', ArticleMembershipViewSet)


urlpatterns = [
    url(r'^$', ArticleMembershipWebListView.as_view(), name='feed'),
    url(r'^numero/$', IssueListView.as_view(), name='issue-list'),
    url(r'^numero/(?P<slug>[-\w]+)/$', IssueDetailView.as_view(), name='issue-detail-site'),
    url(r'^article/(?P<slug>[-\w]+)/$', ArticleDetailView.as_view(), name='article-detail-site'),
    url(r'^(?P<pk>\d+)/$', ArticleMembershipDetailView.as_view(), name='article-membership-detail'),
    url(r'^(?P<pk>\d+).html$', ArticleMembershipDetailRawView.as_view(), name='article-membership-detail-html'),
    url(r'^(?P<pk>\d+).css$', ArticleMembershipDetailCSSView.as_view(), name='article-membership-detail-css'),
    url(r'^(?P<pk>\d+).tpl$', ArticleMembershipDetailTplView.as_view(), name='article-membership-detail-tpl'),

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
