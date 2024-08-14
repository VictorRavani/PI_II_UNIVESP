from flask import Blueprint, render_template
from database.cliente import CLIENTES

cliente_route = Blueprint('cliente', __name__)

"""
Rota de Cliente

    -/clientes/ (GET)- Listar clientes
    -/clientes/ (POST) - inserir o cliente no sevidor 
    -/cliente/new (GET) - renderizar o formulário para criar um cliente
    -/clientes/<id> (GET) - obter os dados dos clientes 
    -/clientes/<id>/edit (GET) - renderizar um formulário para editar um cliente 
    -/clientes/<id>/update (PUT) - atualiza os dados do cliente
    -/clientes/<id>/delete (DELETE) - deleta o registro do usuário 
"""

@cliente_route.route('/')
def lista_clientes():
    """ Listar os clientes """
    return render_template('lista_clientes.html', clientes=CLIENTES)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Inserir os dados do cliente no servidor"""
    pass

@cliente_route.route('/new')
def form_cliente():
    """ Formulário para cadastrar um cliente """
    return render_template('form_cliente.html')

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ Exibir detalher do cliente """
    return render_template('detalhe_cliente.html')

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ Formulario para editar um cliente """
    return render_template('form_edit_cliente.html')


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ atualizar infomações do cliente """
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """ deletar infomações do cliente """
    pass