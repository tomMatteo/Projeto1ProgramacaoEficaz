from flask import Flask, render_template_string, request, redirect
import views


app = Flask(__name__)

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'

@app.route('/')
def index():

    return render_template_string(views.index())

@app.route('/submit', methods=['POST'])
def submit_form():
    titulo = request.form.get('titulo')  
    detalhes = request.form.get('detalhes')  

    views.submit(titulo, detalhes)
    return redirect('/')

@app.route('/delete/<NOTA_ID>', methods=['POST'])
def delete(NOTA_ID):
    views.delete(NOTA_ID)
    return redirect('/')

@app.route('/update/<NOTA_ID>', methods=['GET'])
def view_note(NOTA_ID):
    return render_template_string(views.note_edit(NOTA_ID))

@app.route('/update', methods=['POST'])
def saveup():
    NOTA_ID = request.form.get('NOTA_ID')   
    titulo = request.form.get('titulo')  
    detalhes = request.form.get('detalhes')
    views.save_update(NOTA_ID, titulo, detalhes)
    return redirect('/')
if __name__ == '__main__':
    app.run(debug=True)