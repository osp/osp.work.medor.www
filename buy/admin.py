from django.contrib import admin
from models import RetailOutlet


class RetailOutletAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'name', 'zip_code', 'city')


admin.site.register(RetailOutlet, RetailOutletAdmin)
