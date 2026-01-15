from django.test import TestCase
from django.urls import reverse
from .models import Note


class NoteModelTest(TestCase):
    def setUp(self):
        # Create a Note object for testing
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_has_title(self):
        # Test that a Note object has the expected title
        note = Note.objects.get(id=1)
        self.assertEqual(note.title, 'Test Note')

    def test_note_has_content(self):
        # Test that a Note object has the expected content
        note = Note.objects.get(id=1)
        self.assertEqual(note.content, 'This is a test note.')

    def test_note_str_method(self):
        # Test the __str__ method of the Note model
        note = Note.objects.get(id=1)
        self.assertEqual(str(note), 'Test Note')


class NoteViewTest(TestCase):
    def setUp(self):
        # Create a Note object for testing views
        Note.objects.create(title='Test Note', content='This is a test note.')

    def test_note_list_view(self):
        # Test the note-list view
        response = self.client.get(reverse('all_notes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, "templates/notes/all_notes.html")

    def test_notes_displayed_on_page(self):
        # Test the note-detail view
        response = self.client.get(reverse('all_notes'))

        self.assertContains(response, 'Test Note')
        self.assertContains(response, 'This is a test note.')

    def test_create_note_view(self):
        # Test the note-create view
        response = self.client.post(reverse('note_create'), {
            'title': 'New Note',
            'content': 'Content of the new note.'
        })
        self.assertEqual(Note.objects.count(), 2)
        self.assertRedirects(response, reverse('all_notes'))

    def test_edit_note_view(self):
        # Test the note-edit view
        note = Note.objects.get(id=1)
        response = self.client.post(reverse('note_edit', args=[note.pk]), {
            'title': 'Updated Note',
            'content': 'Updated content of the note.'
        })
        note.refresh_from_db()
        self.assertEqual(note.title, 'Updated Note')
        self.assertEqual(note.content, 'Updated content of the note.')
        self.assertRedirects(response, reverse('all_notes'))

    def test_delete_note_view(self):
        # Test the note-delete view
        note = Note.objects.create(title="Delete Me", content="Soon gone")
        response = self.client.post(reverse('note_delete', args=[note.pk]))
        self.assertEqual(Note.objects.count(), 1)
        self.assertRedirects(response, reverse('all_notes'))
