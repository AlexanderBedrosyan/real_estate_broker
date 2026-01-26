from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('general-terms-of-use/', views.TermsOfUseView.as_view(), name='terms-of-use'),
    path('privacy-policy/', views.PrivacyPolicyView.as_view(), name='privacy-policy'),
    path('cookie-policy/', views.CookiePolicyView.as_view(), name='cookie-policy'),
    path('return-policy/', views.ReturnPolicyView.as_view(), name='return-policy'),
    path('manifest.json', views.manifest, name='manifest'),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots'),
]

