from django.contrib import admin

from note.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description"]
    list_display_links = ["id", "title"]