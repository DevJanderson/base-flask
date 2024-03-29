from flask import Blueprint, render_template

cliente_route = Blueprint('cliente', __name__)

@cliente_route.route('/')
def lista_clientes():
    return render_template('lista_clientes.html')

@cliente_route.route('/', methods=['POST'])
def inserir_cliente():
    """ inserir os dados de cliente no banco de dados """
    pass

@cliente_route.route('/new')
def form_cliente():
    """ formulário para cadastrar um cliente """
    return {'pagina': "formulario clientes"}

@cliente_route.route('/<int:cliente_id>')
def detalhe_cliente(cliente_id):
    """ exibir detalhe do cliente """
    pass

@cliente_route.route('/<int:cliente_id>/edit')
def form_edit_cliente(cliente_id):
    """ formulário para editar um cliente """
    pass

@cliente_route.route('/<int:cliente_id>/update', methods=['PUT'])
def atualizar_cliente(cliente_id):
    """ atualizar informações de cliente """
    pass

@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE'])
def deletar_cliente(cliente_id):
    """ deletar informações de cliente """
    pass