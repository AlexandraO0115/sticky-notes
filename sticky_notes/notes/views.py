from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm

# Create your views here.


def all_notes(request):

    notes = Note.objects.order_by("-created_at")

    context = {
        'notes': notes,
        'page_title': 'All Notes',
    }

    return render(request, 'notes/all_notes.html', context)


def note_create(request):

    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('all_notes')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


def note_edit(request, pk):

    note = get_object_or_404(Note, pk=pk)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.save()
            return redirect('all_notes')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_form.html', {'form': form})


def note_delete(request, pk):

    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
    return redirect('all_notes')
