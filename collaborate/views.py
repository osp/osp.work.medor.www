from .forms import ArticleProposalForm
from django.views.generic.edit import FormView


class ArticleProposalView(FormView):
    template_name = 'collaborate/article_proposal.html'
    form_class = ArticleProposalForm
    success_url = '/thanks/'

    def get_context_data(self, **kwargs):
        context = super(ArticleProposalView, self).get_context_data(**kwargs)
        fields = list(context['form'])
        context['part1'] = fields[:5]
        context['part2'] = fields[5:]
        return context

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ArticleProposalView, self).form_valid(form)
