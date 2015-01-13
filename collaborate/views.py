from .forms import ArticleProposalForm
from django.views.generic.edit import FormView


class ArticleProposalView(FormView):
    template_name = 'collaborate/article_proposal.html'
    form_class = ArticleProposalForm
    success_url = '/thanks/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super(ArticleProposalView, self).form_valid(form)
