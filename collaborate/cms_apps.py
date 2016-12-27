from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

class CollaborateHook(CMSApp):
    name = _("Collaborate")
    urls = ["collaborate.urls"]

apphook_pool.register(CollaborateHook)
