from django.contrib import admin
from models import ArticleProposal
from forms import ArticleProposalForm


class ArticleProposalAdmin(admin.ModelAdmin):
    list_display = ('short_title', 'name', 'creation_date', 'is_answered',)
    list_editable = ('is_answered',)
    list_filter = ('is_answered',)
    date_hierarchy = 'creation_date'


admin.site.register(ArticleProposal, ArticleProposalAdmin)
