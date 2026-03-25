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
        'short_message_preview',
        'picture',
    )

    def short_message_preview(self, obj):
        return obj.short_message[:60] + '…' if len(obj.short_message) > 60 else obj.short_message
    short_message_preview.short_description = 'Message'