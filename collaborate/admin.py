from django.contrib import admin
from models import ArticleProposal
from forms import ArticleProposalForm


class ArticleProposalAdmin(admin.ModelAdmin):
    #form = ArticleProposalForm
    list_display = ('__unicode__', 'name', 'creation_date', 'is_urgent', 'section')
    list_filter = ('is_urgent', 'section')
    date_hierarchy = 'creation_date'


admin.site.register(ArticleProposal, ArticleProposalAdmin)
