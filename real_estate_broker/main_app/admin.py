from django.contrib import admin
from .models import Event, Consultation, Project, Comments


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

@admin.register(Comments)
class CommentsAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'profession',
        'created_at',
    )