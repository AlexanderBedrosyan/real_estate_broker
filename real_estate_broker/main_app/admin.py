from django.contrib import admin
from .models import Event, Consultation


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    pass