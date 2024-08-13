from flask import Flask, url_for, render_template

#ravani

#inicializacao
app = Flask(__name__)

#rotas 
@app.route('/')
def ola_mundo():
    titulo = "Gestão de Usuários"
    usuarios = [
        {"nome": "Guilherme", "membro_ativo": True},
        {"nome": "Julio", "membro_ativo": True},
        {"nome": "Maria", "membro_ativo": False},
    ]
    return render_template ("index.html", titulo=titulo, usuarios=usuarios)

@app.route('/sobre')
def pagina_sobre():
    return """
        <b>ProgramadorPython </b>: assista os vídeos no
        <a href="https://www.youtube.com/watch?v=fkXlSyWiXVg&list=PL39zbyHjgjrbsP3xFSc-YH-6FN8WNpglh&index=2"> Canal no Youtube </a>
    """

#execucao
app.run(debug=True)