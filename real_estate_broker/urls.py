from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from real_estate_broker.main_app.sitemaps import StaticViewSitemap, EventSitemap, ProjectSitemap

sitemaps = {
    'static': StaticViewSitemap,
    'events': EventSitemap,
    'projects': ProjectSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('real_estate_broker.main_app.urls')),
    path('common/', include('real_estate_broker.common.urls')),
    # path('account/', include('real_estate_broker.account.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]

handler404 = "real_estate_broker.main_app.views.error_404_view"
