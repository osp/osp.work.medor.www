from django.views.generic import ListView, DetailView
from .models import Issue, ArticleMembership


class IssueListView(ListView):
    model = Issue


class ArticleMembershipDetailView(DetailView):
    model = ArticleMembership


class ArticleMembershipDetailRawView(DetailView):
    model = ArticleMembership
    template_name = "publish/articlemembership_detail_raw.html"


class ArticleMembershipDetailCSSView(DetailView):
    model = ArticleMembership
    template_name = "publish/articlemembership_detail.css"
    content_type = "text/css; charset=utf-8"


class ArticleMembershipDetailTplView(DetailView):
    model = ArticleMembership
    template_name = "publish/articlemembership_detail.tpl"
    content_type = "text/plain; charset=utf-8"
