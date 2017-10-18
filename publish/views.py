# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.http import Http404

from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend

from .models import Article, Issue, ArticleMembership, ArticleMembershipWeb
from .models import License, Rubric, Contribution, Contributor, Role
from .serializers import RubricSerializer, RoleSerializer, ContributorSerializer, ContributionSerializer, LicenseSerializer, IssueSerializer, ArticleSerializer, ArticleMembershipSerializer


# ViewSets define the view behavior.
class RubricViewSet(viewsets.ModelViewSet):
    queryset = Rubric.objects.all()
    serializer_class = RubricSerializer
    permission_classes = (permissions.IsAdminUser,)


#  ViewSets define the view behavior.
class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = (permissions.IsAdminUser,)


#  ViewSets define the view behavior.
class ContributorViewSet(viewsets.ModelViewSet):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = (permissions.IsAdminUser,)


#  ViewSets define the view behavior.
class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
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


class IssueListView(ListView):
    """
    Archive with all the magazines (not finished yet, and only accessible to superuser)
    """
    model = Issue

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(IssueListView, self).dispatch(*args, **kwargs)


class IssueDetailView(DetailView):
    """
    The Table of Contents for an issue
    """
    model = Issue


class ArticleListView(ListView):
    """
    Archive of articles published on the web
    """
    queryset = Article.objects.filter(published_online=True)
    paginate_by = 10


class ArticleDetailView(DetailView):
    """
    An article
    """
    model = Article

    def get_object(self):
        object = super(ArticleDetailView, self).get_object()
        # object is marked as published online and/or is published on the timeline:
        if object.published_online or object.articlemembershipweb_set.count():
            return object
        # superusers get to read anything
        if self.request.user.is_superuser:
            return object
        # if none of the above, raise a 404
        raise Http404


class ArticleMembershipWebListView(ListView):
    """
    List view for articles published online (the homepage)
    """
    model = ArticleMembershipWeb

    template_name = 'feed.html'
