from django.contrib import admin
from models import ArticleProposal


class ArticleProposalAdmin(admin.ModelAdmin):
    pass
    #list_display = ('__unicode__', 'status', 'email', 'invoice_reference', 'structured_communication', 'old_structured_communication', 'country')
    #list_filter = ('status', 'country')
    #list_editable = ('status',)
    #date_hierarchy = 'creation_date'
    #search_fields = ('first_name', 'last_name', 'status', 'email', 'invoice_reference')
    #actions = [subscription_reminder_first, subscription_reminder_second, subscription_present]


admin.site.register(ArticleProposal, ArticleProposalAdmin)
