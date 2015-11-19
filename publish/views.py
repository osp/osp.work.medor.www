# -*- coding: utf-8 -*-

from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from django.http import Http404
from .models import Article, Issue, ArticleMembership, ArticleMembershipWeb


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


class ArticleMembershipDetailView(DetailView):
    """
    First attempt with Scribe before CKEditor
    """
    model = ArticleMembership

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ArticleMembershipDetailView, self).dispatch(*args, **kwargs)


class ArticleMembershipDetailRawView(DetailView):
    """
    Produce the raw HTML for an ArticleMembership
    """
    model = ArticleMembership
    template_name = "publish/articlemembership_detail_raw.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ArticleMembershipDetailRawView, self).dispatch(*args, **kwargs)


class ArticleMembershipDetailCSSView(DetailView):
    """
    Creates CSS for a specific ArticleMembership to use in HTML2print—
    used for page numbers and running titles.
    """
    model = ArticleMembership
    template_name = "publish/articlemembership_detail.css"
    content_type = "text/css; charset=utf-8"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ArticleMembershipDetailCSSView, self).dispatch(*args, **kwargs)


class ArticleMembershipDetailTplView(DetailView):
    """
    Creates HTML for a specific ArticleMembership to use in HTML2print—
    it’s the shell that loads the necessary libraries and the story.
    """
    model = ArticleMembership
    template_name = "publish/articlemembership_detail.tpl"
    content_type = "text/plain; charset=utf-8"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ArticleMembershipDetailTplView, self).dispatch(*args, **kwargs)
