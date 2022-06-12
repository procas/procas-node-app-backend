from repository import *
from Models.note_response import *


def save_note(email, title, detail) -> NoteResponse:
    try:
        saveNote(email, title, detail)
        return NoteResponse('200', 'Saved')
    except:
        return NoteResponse('500', 'Error while persisting')


def get_notes(email):
    try:
        return getNotes(email)
    except:
        return [{'id': '', 'title': '', 'detail':'', 'date': ''}]

def delete_note(id):
    try:
        deleteNote(id)
        return NoteResponse('200', 'Note Deleted')
    except:
        return NoteResponse('500', 'Error while deleting note')

def modify_note(id, title, detail):
    try:
        modifyNote(id, title, detail)
        return NoteResponse('200', 'Note Updated')
    except:
        return NoteResponse('500', 'Error while updating note')