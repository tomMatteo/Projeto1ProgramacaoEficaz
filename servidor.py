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

@app.route('/update/<NOTA_ID>', methods=['PUT'])
def update(NOTA_ID):
    titulo = request.form.get('titulo')  
    detalhes = request.form.get('detalhes')
    views.update(NOTA_ID)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)