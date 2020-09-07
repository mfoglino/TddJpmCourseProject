import datetime as dt

class Tarjeta(object):

    def __init__(self, numero, nombre,  fecha_vencimiento):
        self.numero = numero
        self.nombre = nombre
        self.fecha_vencimiento = dt.datetime.strptime(fecha_vencimiento, '%m/%y')



class YearMonth:
    def __init__(self, fecha):
        self._fecha = fecha
        self.mes = fecha.month
        self.ano = fecha.year





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
            raise Exception("Ese libro no pertenece a la editorial")

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


class Libro(object):
    def __init__(self, title):
        self.title = title


class Cajero(object):
    def __init__(self, carrito, tarjeta):
        self._carrito = carrito
        self._tarjeta = tarjeta



    def checkout(self):
        if not self._carrito.es_vacio() and self._es_valida():
            return f"Ticket:{self._carrito.total()}"
        else:
            raise Exception("No se puede checkout de carrito vacio")

    def _es_valida(self):
        return self._esta_vencida()

    def _esta_vencida(self):
        now = dt.datetime.now()
        return self._tarjeta.fecha_vencimiento > now

