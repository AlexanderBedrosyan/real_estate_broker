from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, DetailView
from .models import Comments, Consultation, Event, Project
from ..account.models import CustomerModel
from .forms import ConsultationCreateForm

# Create your views here.


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        comments = list(Comments.objects.all())
        first_comment = None
        if comments:
            first_comment = comments.pop()
        context['comments'] = comments
        context['first_comment'] = first_comment

        all_customers = CustomerModel.objects.all()
        customer = all_customers.first() if all_customers else None
        context['customer'] = customer

        return context


class ContactsView(TemplateView):
    template_name = 'contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        all_customers = CustomerModel.objects.all()
        customer = all_customers.first() if all_customers else None
        context['customer'] = customer

        return context


class ConsultationView(CreateView):
    template_name = 'consultation.html'
    model = Consultation
    form_class = ConsultationCreateForm
    success_url = reverse_lazy('home')


class EventsView(ListView):
    template_name = 'events.html'
    model = Event
    paginate_by = 3


class InvestWithMeView(TemplateView):
    template_name = 'invest_with_me.html'


class EventsDetailsView(DetailView):
    pk_url_kwarg = 'pk'
    model = Event
    template_name = 'event_details.html'


class ProjectListView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'object_list'
    paginate_by = 6


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'
    pk_url_kwarg = 'id'