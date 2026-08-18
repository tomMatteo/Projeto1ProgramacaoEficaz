import json
import 
def load_data (data):
    with open(f'static/data/{data}', 'r', encoding='utf-8') as arquivo:
        retorno = json.load(arquivo)
    return retorno
def load_template(template):
    with open(f'static/templates/{template}', 'r', encoding='utf-8') as arquivo:
        retorno = arquivo.read()
    return retorno
def save_data (data):
    with open('static/data/notes.json', 'r+', encoding='utf-8') as arquivo:
        dados = json.load(arquivo)
        dados.append(data)
        arquivo.seek(0)
        json.dump(dados, arquivo, indent=4)