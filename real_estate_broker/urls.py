from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('real_estate_broker.main_app.urls')),
    path('common/', include('real_estate_broker.common.urls')),
]
