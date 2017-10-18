from rest_framework import serializers
from .models import Article, ArticleMembership, Issue, License, Rubric, Contribution, Contributor, Role


class RubricSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Rubric
        fields = '__all__'


class LicenseSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = License
        fields = '__all__'


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Role
        fields = '__all__'


class ContributorSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = Contributor
        fields = '__all__'


class ContributionSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    contributor = ContributorSerializer()
    role = RoleSerializer()
    license = LicenseSerializer()

    class Meta:
        model = Contribution
        fields = ['id', 'contributor', 'role', 'license']


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    rubric = RubricSerializer(required=False)
    contributions = ContributionSerializer(many=True)

    class Meta:
        model = Article
        exclude = ('override_image',)


class ArticleMembershipSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    article = ArticleSerializer()
    folio = serializers.ReadOnlyField()

    class Meta:
        model = ArticleMembership
        depth = 1
        fields = '__all__'


class IssueSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    articlemembership_set = ArticleMembershipSerializer(many=True)

    class Meta:
        model = Issue
        fields = '__all__'
