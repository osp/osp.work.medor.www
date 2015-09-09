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
    content_type = "text/css"


class ArticleMembershipDetailTplView(DetailView):
    model = ArticleMembership
    template_name = "publish/articlemembership_detail.tpl"
    content_type = "text/css"
