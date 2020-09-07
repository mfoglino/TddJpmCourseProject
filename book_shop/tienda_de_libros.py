class Carrito(object):

    _carrito = []
    _catalogo = ["un libro", "otro libro"]


    def __init__(self):
        pass

    def es_vacio(self):
        return len(self._carrito) == 0

    def add_libro(self, libro):
        if libro in self._catalogo:
            self._carrito.append(libro)
        else:
            raise Exception("Ese libro no pertenece a la editorial")

    def contiene(self, libro):
        return libro in self._carrito


class Libro(object):
    def __init__(self, title):
        self.title = title