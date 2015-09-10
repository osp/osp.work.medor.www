from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView
from .models import Issue, ArticleMembership


class IssueListView(ListView):
    model = Issue

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(IssueListView, self).dispatch(*args, **kwargs)


class ArticleMembershipDetailView(DetailView):
    model = ArticleMembership

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ArticleMembershipDetailView, self).dispatch(*args, **kwargs)


class ArticleMembershipDetailRawView(DetailView):
    model = ArticleMembership
    template_name = "publish/articlemembership_detail_raw.html"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ArticleMembershipDetailRawView, self).dispatch(*args, **kwargs)


class ArticleMembershipDetailCSSView(DetailView):
    model = ArticleMembership
    template_name = "publish/articlemembership_detail.css"
    content_type = "text/css; charset=utf-8"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ArticleMembershipDetailCSSView, self).dispatch(*args, **kwargs)


class ArticleMembershipDetailTplView(DetailView):
    model = ArticleMembership
    template_name = "publish/articlemembership_detail.tpl"
    content_type = "text/plain; charset=utf-8"

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ArticleMembershipDetailTplView, self).dispatch(*args, **kwargs)
