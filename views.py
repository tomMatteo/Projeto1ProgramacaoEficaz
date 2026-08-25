from utils import load_data, load_template, save_data, remove_data
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