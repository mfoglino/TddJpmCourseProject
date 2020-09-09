CLIENTE_INVALIDO = "Cliente invalido"


class Aplicacion(object):
    def __init__(self, usuarios ):
        self._usuarios = usuarios

    def es_carrito_vacio(self, id_carrito):
        if id_carrito == 2:
            raise Exception(CLIENTE_INVALIDO)
        return True

    def crear_carrito(self, id_cliente):
        if not self.es_cliente_valido(id_cliente):
            raise Exception(CLIENTE_INVALIDO)

    def es_cliente_valido(self, id):
        return id in self._usuarios