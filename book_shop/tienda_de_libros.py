import datetime as dt

ERROR_CHECKOUT_DE_CARRITO_VACIO = "No se puede checkout de carrito vacio"

ERROR_NO_PERTENECE_A_LA_EDITORIAL = "Ese libro no pertenece a la editorial"

ERROR_TARJETA_VENCIDA = "Error, tarjeta vencida!"

ERROR_TARJETA_SIN_CREDITO = "TARJETA SIN CREDITO"

ERROR_MERCHANT_CAIDO = "ERROR: MERCHANT CAIDO"

MERCHANT_SIN_CONEXION = "Error: Merchant sin conexion"

MERCHANT_SIN_CREDITO = "Error: Tarjeta sin credito"

ERROR_CARRITO_EXPIRADO = "ERRRO: CARRITO EXPIRADO"


class Tarjeta(object):

    def __init__(self, numero, nombre,  fecha_vencimiento):
        self.numero = numero
        self.nombre = nombre
        self.fecha_vencimiento = dt.datetime.strptime(fecha_vencimiento, '%m/%y')



class Carrito(object):

    def __init__(self, catalogo):
        self._carrito = []
        self._catalogo = catalogo

    def es_vacio(self):
        return len(self._carrito) == 0

    def add(self, libro, cantidad=1):
        if self.esta_en_catalogo(libro):
            for _ in range(cantidad):
                self._carrito.append(libro)
        else:
            raise Exception(ERROR_NO_PERTENECE_A_LA_EDITORIAL)

    def contiene(self, libro):
        return libro in self._carrito

    def total(self):
        sum = 0
        for libro in self._carrito:
            sum += self._precio_libro(libro)
        return sum

    def _precio_libro(self, libro):
        if libro in self._catalogo:
            return self._catalogo[libro]

    def esta_en_catalogo(self, libro):
        return libro in self._catalogo



class Libro:
    def __init__(self, title):
        self.title = title



class Cajero:

    def __init__(self, carrito, tarjeta, merchant):
        self._carrito = carrito
        self._tarjeta = tarjeta
        self._merchant = merchant


    def checkout(self):
        self.assert_carrito_no_vacio()

        self.assert_tarjeta_no_valido()


        self._merchant.debito(self._carrito.total(), self._tarjeta)

        return f"Ticket:{self._carrito.total()}"

    def assert_tarjeta_no_valido(self):
        if not self._es_valida():
            raise Exception(ERROR_TARJETA_VENCIDA)

    def assert_carrito_no_vacio(self):
        if self._carrito.es_carrito_vacio():
            raise Exception(ERROR_CHECKOUT_DE_CARRITO_VACIO)

    def _es_valida(self):
        return not self._esta_vencida()

    def _esta_vencida(self):
        now = dt.datetime.now()
        return self._tarjeta.fecha_vencimiento < now


from abc import ABC

class Merchant(ABC):
    def debito(self, amount, tarjeta):
        pass


class MerchantOK(Merchant):
    def debito(self, amount, tarjeta):
        return "OK"


class MerchantNoCredit(Merchant):
    def debito(self, amount, tarjeta):
        raise Exception(ERROR_TARJETA_SIN_CREDITO)


class MerchantCaido(Merchant):
    def debito(self, amount, tarjeta):
        raise Exception(ERROR_MERCHANT_CAIDO)