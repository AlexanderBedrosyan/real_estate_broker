from django.urls import path
from . import views

urlpatterns = [
    path('general-terms-of-use/', views.TermsOfUseView.as_view(), name='terms-of-use'),
    path('privacy-policy/', views.PrivacyPolicyView.as_view(), name='privacy-policy'),
]
