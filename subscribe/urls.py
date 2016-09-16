from django.conf.urls import patterns, url
from subscribe.views import CooperationWizardView, SubscriptionWizardView, subscribers_as_csv, cooperators_as_csv, OrderWizardView


urlpatterns = patterns('',
    url(r'^cooperation/$', CooperationWizardView.as_view(), name='cooperate-wizard'),
    url(r'^abonnement/$', SubscriptionWizardView.as_view(), name='subscribe-wizard'),
    url(r'^subscribers/$', subscribers_as_csv, name='subscribers-as-csv'),
    url(r'^cooperators/$', cooperators_as_csv, name='cooperators-as-csv'),
    url(r'^order/$', OrderWizardView.as_view(), name='order-wizard'),
)
