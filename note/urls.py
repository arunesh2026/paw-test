from django.urls import path

from note.views import create_note, list_note


urlpatterns = [
    path("add/", view=create_note, name="create_note"),
    path("list/", view=list_note, name="list_note"),
]
