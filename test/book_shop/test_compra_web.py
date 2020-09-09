import pytest

from book_shop.mi_applicacion import Aplicacion, CLIENTE_INVALIDO, PASSWORD_INVALIDA


def get_usuarios():
    usuarios = {}
    usuarios['pepe'] = '123'
    usuarios['flor'] = '1234'
    usuarios['natacha'] = '1236'
    return usuarios

def test_cuando_creo_carrito_esta_vacio():
    app = Aplicacion(get_usuarios())

    id_cliente = "pepe"
    id_carrito = app.crear_carrito(id_cliente, "123")
    assert app.es_carrito_vacio(id_carrito)



def test_no_puedo_crear_un_carrito_con_un_cliente_invalido():
    app = Aplicacion(get_usuarios())

    with pytest.raises(Exception, match=CLIENTE_INVALIDO):
        id_cliente_invalido = "id666"
        id_carrito = app.crear_carrito(id_cliente_invalido, "no importa")


def test_un_cliente_con_password_no_valida_no_puedo_crear_un_carrito():
    app = Aplicacion(get_usuarios())

    with pytest.raises(Exception, match=PASSWORD_INVALIDA):
        id_cliente_invalido = "pepe"
        id_carrito = app.crear_carrito(id_cliente_invalido, "password incorrecta")