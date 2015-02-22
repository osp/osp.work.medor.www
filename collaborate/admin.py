from django.contrib import admin
from models import ArticleProposal
from forms import ArticleProposalForm


class ArticleProposalAdmin(admin.ModelAdmin):
    form = ArticleProposalForm
    list_display = ('__unicode__', 'creation_date')
    #list_filter = ('status', 'country')
    #list_editable = ('status',)
    #date_hierarchy = 'creation_date'
    #search_fields = ('first_name', 'last_name', 'status', 'email', 'invoice_reference')
    #actions = [subscription_reminder_first, subscription_reminder_second, subscription_present]


admin.site.register(ArticleProposal, ArticleProposalAdmin)
