from django.urls import path
from .views import (
    all_notes,
    note_create,
    note_edit,
    note_delete,
)

urlpatterns = [
    # URL pattern for displaying all notes
    path("", all_notes, name="all_notes"),

    # URL pattern for creating a new note
    path("note/new/", note_create, name="note_create"),

    # URL pattern for editing an existing note
    path("note/<int:pk>/edit/", note_edit, name="note_edit"),

    # URL pattern for deleting an existing note
    path("note/<int:pk>/delete/", note_delete, name="note_delete"),
]
