import json
import sqlite3
# def load_data (data):
#     with open(f'static/data/{data}', 'r', encoding='utf-8') as arquivo:
#         retorno = json.load(arquivo)
#     return retorno
def load_data ():
    conn = sqlite3.connect('banco.db')
    curs = conn.cursor()
    curs.execute("SELECT rowid,title,content FROM note ORDER BY favorite")
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
    curs.execute(''' INSERT INTO note(title,content, favorite)
            VALUES(?,?,?) ''', (data['titulo'], data['detalhes'], 0))
    conn.commit()
    conn.close()
def remove_data (data):
    conn = sqlite3.connect('banco.db')
    curs = conn.cursor()
    curs.execute(''' DELETE FROM note WHERE rowid = ?''', (data,))
    conn.commit()
    conn.close()
# def turn_to_sql ():
#     dados = load_data('notes.json')
#     conn = sqlite3.connect('banco.db')
#     curs = conn.cursor()
#     curs.execute('''CREATE TABLE note(
#       title varchar(255), 
#       content varchar(255),
#       favorite integer
#     );
#     ''')
#     for dado in dados:
#         title = dado['titulo']
#         content = dado['detalhes']
#         curs.execute(''' INSERT INTO note(title,content, favorite)
#               VALUES(?,?,?) ''', (title, content, 0))
#     conn.commit()
#     conn.close()
# turn_to_sql()