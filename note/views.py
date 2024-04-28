from django.shortcuts import render, redirect

from note.models import Note
from note.forms import NoteForm


def create_note(request):
    
    if request.method == "POST":
        form = NoteForm(request.POST)
        
        if form.is_valid():
            form.save()
            
    context = {
        "form": NoteForm()
    }
    
    return render(request=request, template_name="note/add-note.html", context=context)


def list_note(request):
    notes = Note.objects.all()
    
    context = {
        "notes": notes
    }
    
    return render(request=request, template_name="note/list.html", context=context)