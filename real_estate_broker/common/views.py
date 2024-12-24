from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class TermsOfUseView(TemplateView):
    template_name = 'common/terms_of_use.html'