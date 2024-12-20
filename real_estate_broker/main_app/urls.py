from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('\contacts', views.ContactsView.as_view(), name='contacts'),
]
