from django.template.loader import render_to_string
from django.views.generic.edit import FormView
from django.views.generic import ListView, DetailView
from .forms import ArticleProposalForm, ArticleProposalSimpleForm
from .models import ArticleProposal
from django.core import urlresolvers
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import user_passes_test
from django.contrib.sites.shortcuts import get_current_site


class ArticleProposalThanksView(TemplateView):
    template_name = "collaborate/article_proposal_thanks.html"


class ArticleProposalBaseView(FormView):
    success_url = reverse_lazy('article-proposal-thanks')

    def form_valid(self, form):
        form.save()
        obj = form.instance
        site = get_current_site(self.request)
        admin_url = u"https://%s%s" % (site, urlresolvers.reverse('admin:collaborate_articleproposal_change', args=(obj.id,)))

        subject = "Nouvelle demande de collaboration"
        message = render_to_string('collaborate/article_proposal_alert.txt', {'obj': obj, 'admin_url': admin_url})
        sender = "jaiuntrucpourvous@medor.coop"
        recipients = ["jaiuntrucpourvous@medor.coop"]
        send_mail(subject, message, sender, recipients)

        subject = "Demande de collaboration"
        message = render_to_string('collaborate/article_proposal_confirmation.txt', {'obj': obj})
        sender = "jaiuntrucpourvous@medor.coop"
        recipients = [obj.email]
        send_mail(subject, message, sender, recipients)

        return super(ArticleProposalBaseView, self).form_valid(form)


class ArticleProposalView(ArticleProposalBaseView):
    template_name = 'collaborate/article_proposal.html'
    form_class = ArticleProposalForm


class ArticleProposalSimpleView(ArticleProposalBaseView):
    template_name = 'collaborate/article_proposal_simple.html'
    form_class = ArticleProposalSimpleForm


def can_read_proposals(user):
    """docstring for can_read_proposals"""
    return user.groups.filter(name='Collaboration').exists()


class ArticleProposalListView(ListView):
    model = ArticleProposal

    @method_decorator(user_passes_test(can_read_proposals))
    def dispatch(self, *args, **kwargs):
        return super(ArticleProposalListView, self).dispatch(*args, **kwargs)

class ArticleProposalDetailView(DetailView):
    model = ArticleProposal

    @method_decorator(user_passes_test(can_read_proposals))
    def dispatch(self, *args, **kwargs):
        return super(ArticleProposalDetailView, self).dispatch(*args, **kwargs)
