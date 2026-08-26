from utils import load_data, load_template, save_data, remove_data, load_one, update_data
import json

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id= dados[2], title=dados[0], details=dados[1])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)
    return load_template('index.html').format(notes=notes)

def submit (titulo, detalhes):
    save_data({"titulo": titulo, "detalhes": detalhes})

def delete (NOTA_ID):
    remove_data(NOTA_ID)

def note_edit (NOTA_ID):
    note_template = load_template('edit.html')
    dados = load_one(NOTA_ID)
    return note_template.format(title=dados[0], details=dados[1], id=dados[2])

def save_update(NOTA_ID, titulo, detalhes):
    update_data({"id": NOTA_ID,"titulo": titulo, "detalhes": detalhes})