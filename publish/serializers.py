from rest_framework import serializers
from .models import Article, ArticleMembership, Issue, License, Rubric, Contribution, Contributor, Role


class RubricSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:rubric-detail")
    id = serializers.ReadOnlyField()

    class Meta:
        model = Rubric
        fields = '__all__'


class LicenseSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:license-detail")
    id = serializers.ReadOnlyField()

    class Meta:
        model = License
        fields = '__all__'


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:role-detail")
    id = serializers.ReadOnlyField()

    class Meta:
        model = Role
        fields = '__all__'


class ContributorSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:contributor-detail")
    id = serializers.ReadOnlyField()

    class Meta:
        model = Contributor
        exclude = ('image',)


class ContributionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:contribution-detail")
    id = serializers.ReadOnlyField()
    contributor = ContributorSerializer()
    role = RoleSerializer()
    license = LicenseSerializer()

    class Meta:
        model = Contribution
        fields = ['url', 'id', 'contributor', 'role', 'license']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:article-detail")
    id = serializers.ReadOnlyField()
    rubric = RubricSerializer(required=False)
    contributions = ContributionSerializer(many=True)
    license = LicenseSerializer()

    class Meta:
        model = Article
        exclude = ('override_image',)


class ArticleMembershipSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:articlemembership-detail")
    id = serializers.ReadOnlyField()
    article = ArticleSerializer()
    folio = serializers.ReadOnlyField()

    class Meta:
        model = ArticleMembership
        depth = 1
        exclude = ('issue',)


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:issue-detail")
    id = serializers.ReadOnlyField()
    articlemembership_set = ArticleMembershipSerializer(many=True)

    class Meta:
        model = Issue
        fields = '__all__'
