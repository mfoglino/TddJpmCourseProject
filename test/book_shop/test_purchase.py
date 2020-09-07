import pytest

from book_shop.tienda_de_libros import Carrito, Libro, Cajero


def catalogo():
    return [("un libro", 5), ("otro libro", 10)]



def test_carrito_vacio():
    carrito = Carrito(catalogo())
    assert carrito.es_vacio()


def test_carrito_con_un_item():
    carrito = Carrito(catalogo())

    libro = "un libro"
    carrito.add(libro)

    assert not carrito.es_vacio()
    assert carrito.contiene(libro)

def test_carrito_dos_del_mismo():
    carrito = Carrito(catalogo())

    libro = "un libro"
    uno_mas = "un libro"
    #carrito.add_libro(libro)
    #carrito.add_libro(uno_mas)

    cantidad = 2
    carrito.add(libro, cantidad)

    assert not carrito.es_vacio()
    assert carrito.contiene(libro)
    assert carrito.contiene(uno_mas)


def test_carrito_con_mas_de_un_item():
    carrito = Carrito(catalogo())

    libro = "un libro"
    otro_libro = "otro libro"
    carrito.add(libro)
    carrito.add(otro_libro)

    assert not carrito.es_vacio()
    assert carrito.contiene(libro)
    assert carrito.contiene(otro_libro)




def test_editorial():
    carrito = Carrito(catalogo())

    no_editorial_libro = "un libro de no la editorial"

    with pytest.raises(Exception, match="Ese libro no pertenece a la editorial"):
        carrito.add(no_editorial_libro)




def test_el_carrito_tiene_total_correcto():
    carrito = Carrito(catalogo())

    libro = "un libro"

    carrito.add(libro)

    assert carrito.total() == 5




def test_checkout_carrito_ok():
    carrito = Carrito(catalogo())

    libro = "un libro"

    carrito.add(libro)

    cajero = Cajero(carrito)

    ticket_con_total = "Ticket:5"
    assert cajero.checkout() == ticket_con_total



def test_no_se_puede_checkout_carrito_vacio():
    carrito = Carrito(catalogo())

    cajero = Cajero(carrito)

    with pytest.raises(Exception, match="No se puede checkout de carrito vacio"):
        cajero.checkout()





