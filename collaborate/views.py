from django.template.loader import render_to_string
from django.views.generic.edit import FormView
from .forms import ArticleProposalForm
from django.core import urlresolvers
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView


class ArticleProposalThanksView(TemplateView):
    template_name = "collaborate/article_proposal_thanks.html"


class ArticleProposalView(FormView):
    template_name = 'collaborate/article_proposal.html'
    form_class = ArticleProposalForm
    success_url = reverse_lazy('article-proposal-thanks')

    def get_context_data(self, **kwargs):
        context = super(ArticleProposalView, self).get_context_data(**kwargs)
        fields = list(context['form'])
        context['part1'] = fields[:4]
        context['part2'] = fields[4:5]
        context['part3'] = fields[5:]
        return context

    def form_valid(self, form):
        form.save()
        obj = form.instance
        admin_url = urlresolvers.reverse('admin:collaborate_articleproposal_change', args=(obj.id,))

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

        return super(ArticleProposalView, self).form_valid(form)
