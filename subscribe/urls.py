from django.conf.urls import patterns, url
from subscribe.views import CooperationWizardView, SubscriptionWizardView, HomePageView, FAQPageView, subscribers_as_csv


urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home-page'),
    url(r'^FAQ/$', FAQPageView.as_view(), name='faq-page'),
    url(r'^cooperation/$', CooperationWizardView.as_view(), name='cooperate-wizard'),
    url(r'^abonnement/$', SubscriptionWizardView.as_view(), name='subscribe-wizard'),
    url(r'^subscribers/$', subscribers_as_csv, name='subscribers-as-csv'),
)
