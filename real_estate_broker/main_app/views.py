from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Comments

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

        return context
