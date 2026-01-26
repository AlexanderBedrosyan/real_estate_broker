from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Event, Project


class StaticViewSitemap(Sitemap):
    """Sitemap for static pages"""
    protocol = 'https'
    
    def items(self):
        # Returns list of tuples: (url_name, priority, changefreq)
        return [
            ('home', 1.0, 'daily'),
            ('projects', 0.9, 'weekly'),
            ('events', 0.9, 'weekly'),
            ('consultation', 0.8, 'monthly'),
            ('invest-with-me', 0.8, 'monthly'),
            ('contacts', 0.7, 'monthly'),
        ]

    def location(self, item):
        return reverse(item[0])
    
    def priority(self, item):
        return item[1]
    
    def changefreq(self, item):
        return item[2]


class EventSitemap(Sitemap):
    """Sitemap for event pages"""
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Event.objects.all().order_by('-date')

    def lastmod(self, obj):
        return obj.date


class ProjectSitemap(Sitemap):
    """Sitemap for project pages"""
    changefreq = 'weekly'
    priority = 0.8
    protocol = 'https'

    def items(self):
        return Project.objects.all().order_by('-created_at')

    def lastmod(self, obj):
        return obj.created_at
