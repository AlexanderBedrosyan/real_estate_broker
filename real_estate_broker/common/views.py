from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class TermsOfUseView(TemplateView):
    template_name = 'common/terms_of_use.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'common/privacy_policy.html'


class CookiePolicyView(TemplateView):
    template_name = 'common/cookie_policy.html'


class ReturnPolicyView(TemplateView):
    template_name = 'common/return_policy.html'