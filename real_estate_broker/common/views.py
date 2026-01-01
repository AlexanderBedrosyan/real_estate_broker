from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.http import require_GET
import json
import os
from django.conf import settings


# Create your views here.
@require_GET
def manifest(request):
    """Serve the web app manifest for PWA support"""
    manifest_path = os.path.join(settings.BASE_DIR, 'static', 'manifest.json')
    try:
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest_data = json.load(f)
        return JsonResponse(manifest_data, content_type='application/manifest+json')
    except FileNotFoundError:
        return JsonResponse({'error': 'Manifest not found'}, status=404)


class TermsOfUseView(TemplateView):
    template_name = 'common/terms_of_use.html'


class PrivacyPolicyView(TemplateView):
    template_name = 'common/privacy_policy.html'


class CookiePolicyView(TemplateView):
    template_name = 'common/cookie_policy.html'


class ReturnPolicyView(TemplateView):
    template_name = 'common/return_policy.html'