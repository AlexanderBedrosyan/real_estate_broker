from django.contrib import admin
from .models import Event, Consultation, Project


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = (
    'first_name', 
    'last_name',
    'email'
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )