import pytest

from book_shop.tienda_de_libros import Carrito, Cajero, Tarjeta, ERROR_TARJETA_VENCIDA, \
    ERROR_NO_PERTENECE_A_LA_EDITORIAL, ERROR_CHECKOUT_DE_CARRITO_VACIO, ERROR_TARJETA_SIN_CREDITO, \
    ERROR_MERCHANT_CAIDO, \
    MerchantNoCredit, \
    MerchantOK, MerchantCaido, ERROR_CARRITO_EXPIRADO




def catalogo():
    catalogo = {}
    catalogo["un libro"] = 5
    catalogo["otro libro"] = 10
    return catalogo


def get_merchant():
    return MerchantOK()


def get_merchant_sin_credito():
    return MerchantNoCredit()


def get_merchant_caido():
    return MerchantCaido()


# =======================================================


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
    # carrito.add_libro(libro)
    # carrito.add_libro(uno_mas)

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

    with pytest.raises(Exception, match=ERROR_NO_PERTENECE_A_LA_EDITORIAL):
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

    tarjeta = Tarjeta("0001", "Juan Pepe", '08/22')
    cajero = Cajero(carrito, tarjeta, get_merchant())

    ticket_con_total = "Ticket:5"
    assert cajero.checkout() == ticket_con_total


def test_no_se_puede_checkout_carrito_vacio():
    carrito = Carrito(catalogo())

    tarjeta = Tarjeta("0001", "Juan Pepe", '08/22')
    cajero = Cajero(carrito, tarjeta, get_merchant())

    with pytest.raises(Exception, match=ERROR_CHECKOUT_DE_CARRITO_VACIO):
        cajero.checkout()



def test_no_se_puede_checkout_con_tarjeta_vencida():
    carrito = Carrito(catalogo())
    libro = "un libro"
    carrito.add(libro)

    tarjeta = Tarjeta("0001", "Juan Pepe", '11/19')
    cajero = Cajero(carrito, tarjeta, get_merchant())

    with pytest.raises(Exception, match=ERROR_TARJETA_VENCIDA):
        cajero.checkout()


def test_transaccion_existosa():
    carrito = Carrito(catalogo())
    libro = "un libro"
    carrito.add(libro)

    tarjeta = Tarjeta("0001", "Juan Pepe", '11/22')

    merchant = get_merchant()
    cajero = Cajero(carrito, tarjeta, get_merchant())
    assert cajero.checkout() == "Ticket:5"


def test_error_al_transaccion_tarjeta_sin_credito():
    carrito = Carrito(catalogo())
    libro = "un libro"
    carrito.add(libro)

    tarjeta = Tarjeta("0001", "Juan Pepe", '11/22')

    merchant = get_merchant()
    cajero = Cajero(carrito, tarjeta, get_merchant_sin_credito())

    with pytest.raises(Exception, match=ERROR_TARJETA_SIN_CREDITO):
        cajero.checkout()


def test_error_al_transaccion_merchant_caido():
    carrito = Carrito(catalogo())
    libro = "un libro"
    carrito.add(libro)

    tarjeta = Tarjeta("0001", "Juan Pepe", '11/22')

    merchant = get_merchant()
    cajero = Cajero(carrito, tarjeta, get_merchant_caido())

    with pytest.raises(Exception, match=ERROR_MERCHANT_CAIDO):
        cajero.checkout()

