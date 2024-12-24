from django.urls import path
from . import views

urlpatterns = [
    path('general-terms-of-use/', views.TermsOfUseView.as_view(), name='terms-of-use'),
]
