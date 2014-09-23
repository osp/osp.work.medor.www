from django.conf.urls import patterns, url
from subscribe.views import CooperationWizardView, SubscriptionWizardView, HomePageView


urlpatterns = patterns('',
    url(r'^$', HomePageView.as_view(), name='home-page'),
    url(r'^cooperation/$', CooperationWizardView.as_view(), name='cooperate-wizard'),
    url(r'^abonnement/$', SubscriptionWizardView.as_view(), name='subscribe-wizard'),
)
