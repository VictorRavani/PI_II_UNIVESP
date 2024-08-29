from flask import Blueprint, render_template, request
import requests
from database.models.cliente import Cliente

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
    clientes = Cliente.select()
    print('lista_clientes: ', clientes)
    return render_template('lista_clientes.html', clientes=clientes)

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ Inserir os dados do cliente no servidor"""
    
    data = request.json

    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email'],
    )

    return render_template('item_cliente.html', cliente=novo_usuario)

@cliente_route.route('/new')
def form_cliente():
    """ Formulário para cadastrar um cliente """
    return render_template('form_cliente.html')



@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ Exibir detalher do cliente """

    cliente = Cliente.get_by_id(cliente_id)
    return render_template('detalhe_cliente.html', cliente=cliente)



@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ Formulario para editar um cliente """
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('form_cliente.html', cliente=cliente)


@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ atualizar infomações do cliente """

    # obter dados do formulário de edição 
    data = request.json

    cliente_editado = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save() 

    # editar usuario        
    return render_template('item_cliente.html', cliente=cliente_editado)



@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """ deletar infomações do cliente """
    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {'deletec': 'ok'}


@cliente_route.route('/pesquisa-cep')
def listar_ceps():
    """Listar os dados do CEP"""

    cep = '05131110'
    cep = cep.replace("-", "").replace(".", "").replace(" ", "")

    # Inicializa variáveis
    uf, cidade, bairro, mensagem_erro = None, None, None, None

    if len(cep) == 8:
        # Consulta o CEP se fornecido
        try:
            link = f'https://viacep.com.br/ws/{cep}/json/'
            requisicao = requests.get(link)
            dic_requisicao = requisicao.json()

            # Verifica se a resposta contém erros
            if dic_requisicao.get('erro'):
                mensagem_erro = "CEP não encontrado. Verifique o CEP e tente novamente."
            else:
                uf = dic_requisicao.get('uf')
                cidade = dic_requisicao.get('localidade')
                bairro = dic_requisicao.get('bairro')

        except requests.RequestException as e:
            mensagem_erro = f"Erro ao consultar o CEP: {e}"
    else:
        mensagem_erro = "CEP inválido. O CEP deve conter 8 dígitos."

    # Passa os dados e a mensagem de erro para o template
    return render_template('pesquisa_cep.html', uf=uf, cidade=cidade, bairro=bairro, mensagem_erro=mensagem_erro)