from utils import load_data, load_template, save_data
import json

def index():
    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados[0], details=dados[1])
        for dados in load_data()
    ]
    notes = '\n'.join(notes_li)

    return load_template('index.html').format(notes=notes)

def submit (titulo, detalhes):
    save_data({"titulo": titulo, "detalhes": detalhes})