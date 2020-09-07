import pytest

from book_shop.tienda_de_libros import Carrito, Libro


def test_carrito_vacio():
    carrito = Carrito()
    assert carrito.es_vacio()


def test_carrito_con_un_item():
    carrito = Carrito()

    libro = "un libro"
    carrito.add_libro(libro)

    assert not carrito.es_vacio()
    assert carrito.contiene(libro)

def test_carrito_dos_del_mismo():
    carrito = Carrito()

    libro = "un libro"
    uno_mas = "un libro"
    carrito.add_libro(libro)
    carrito.add_libro(uno_mas)

    assert not carrito.es_vacio()
    assert carrito.contiene(libro)
    assert carrito.contiene(uno_mas)


def test_carrito_con_mas_de_un_item():
    carrito = Carrito()

    libro = "un libro"
    otro_libro = "otro libro"
    carrito.add_libro(libro)
    carrito.add_libro(otro_libro)

    assert not carrito.es_vacio()
    assert carrito.contiene(libro)
    assert carrito.contiene(otro_libro)




def test_editorial():
    carrito = Carrito()

    no_editorial_libro = "un libro de no la editorial"

    with pytest.raises(Exception, match="Ese libro no pertenece a la editorial"):
        carrito.add_libro(no_editorial_libro)



