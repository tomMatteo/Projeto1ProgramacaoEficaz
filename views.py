from utils import load_data, load_template, save_data, remove_data
import json

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(id= dados[0], title=dados[1], details=dados[2])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)
    return load_template('index.html').format(notes=notes)

def submit (titulo, detalhes):
    save_data({"titulo": titulo, "detalhes": detalhes})

def delete (NOTA_ID):
    remove_data(NOTA_ID)