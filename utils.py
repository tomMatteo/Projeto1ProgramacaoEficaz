import json
import sqlite3
# def load_data (data):
    # with open(f'static/data/{data}', 'r', encoding='utf-8') as arquivo:
        # retorno = json.load(arquivo)
    # return retorno
def load_data ():
    conn = sqlite3.connect('banco.db')
    curs = conn.cursor()
    curs.execute("SELECT title,details FROM notas ORDER BY favorite")
    retorno = curs.fetchall()
    conn.close()
    return retorno
def load_template(template):
    with open(f'static/templates/{template}', 'r', encoding='utf-8') as arquivo:
        retorno = arquivo.read()
    return retorno
# def save_data (data):
#     with open('static/data/notes.json', 'r+', encoding='utf-8') as arquivo:
#         dados = json.load(arquivo)
#         dados.append(data)
#         arquivo.seek(0)
#         json.dump(dados, arquivo, indent=4)
def save_data (data):
    conn = sqlite3.connect('banco.db')
    curs = conn.cursor()
    curs.execute(''' INSERT INTO notas(title,details, favorite)
            VALUES(?,?,?) ''', (data['titulo'], data['detalhes'], 0))
    curs.execute(''' DELETE from notas WHERE favorite is NULL ''')
    conn.commit()
    conn.close()
# def turn_to_sql ():
#     dados = load_data('notes.json')
#     conn = sqlite3.connect('banco.db')
#     curs = conn.cursor()
#     curs.execute('''CREATE TABLE notas(
#       id ROWID, 
#       title varchar(255), 
#       details varchar(255),
#       favorite integer
#     );
#     ''')
#     for dado in dados:
#         title = dado['titulo']
#         details = dado['detalhes']
#         curs.execute(''' INSERT INTO notas(title,details, favorite)
#               VALUES(?,?,?) ''', (title, details, 0))
#     conn.commit()
#     conn.close()