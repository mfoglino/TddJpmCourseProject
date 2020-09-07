


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
        for i in self._catalogo:
            if i[0] == libro:
                return i[1]




    def esta_en_catalogo(self, libro):
        for l in self._catalogo:
            if l[0] == libro:
                return True

        return False




class Libro(object):
    def __init__(self, title):
        self.title = title



class Cajero(object):
    def __init__(self, carrito):
        self._carrito = carrito

    def checkout(self):
        if not self._carrito.es_vacio():
            return f"Ticket:{self._carrito.total()}"
        else:
            raise Exception("No se puede checkout de carrito vacio")
