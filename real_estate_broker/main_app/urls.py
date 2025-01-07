from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('contacts', views.ContactsView.as_view(), name='contacts'),
    path('consultation', views.ConsultationView.as_view(), name='consultation'),
    path('events', views.EventsView.as_view(), name='events'),
    path('event-details//<int:pk>', views.EventsDetailsView.as_view(), name='event-details'),
    path('invest-with-me', views.InvestWithMeView.as_view(), name='invest-with-me'),
]
