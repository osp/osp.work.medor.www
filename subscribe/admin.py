from django.contrib import admin
from subscribe.models import Subscription, Cooperation


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'status', 'invoice_reference', 'structured_communication')
    list_filter = ('status',)


class CooperationAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'status', 'invoice_reference', 'structured_communication')
    list_filter = ('status',)


admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Cooperation, CooperationAdmin)
