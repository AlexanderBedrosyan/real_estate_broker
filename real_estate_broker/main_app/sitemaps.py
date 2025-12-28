from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Event, Project


class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'weekly'

    def items(self):
        return ['home', 'events', 'projects', 'consultation', 'invest_with_me', 'contacts']

    def location(self, item):
        return reverse(item)


class EventSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Event.objects.all().order_by('-pk')

    def lastmod(self, obj):
        return getattr(obj, 'updated_at', None) or getattr(obj, 'created_at', None)


class ProjectSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.7

    def items(self):
        return Project.objects.all().order_by('-pk')

    def lastmod(self, obj):
        return getattr(obj, 'updated_at', None) or getattr(obj, 'created_at', None)
