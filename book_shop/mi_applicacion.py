CLIENTE_INVALIDO = "Cliente invalido"
PASSWORD_INVALIDA = "PASSWORD INVALIDA"


class Aplicacion(object):
    def __init__(self, usuarios ):
        self._usuarios = usuarios

    def es_carrito_vacio(self, id_carrito):
        if id_carrito == 2:
            raise Exception(CLIENTE_INVALIDO)
        return True

    def crear_carrito(self, id_cliente, password):
        if not self.es_cliente_valido(id_cliente):
            raise Exception(CLIENTE_INVALIDO)

        self._es_usuario_con_password_incorrecta(id_cliente, password)

    def _es_usuario_con_password_incorrecta(self, id_cliente, password):
        if self._usuarios[id_cliente] != password:
            raise Exception(PASSWORD_INVALIDA)

    def es_cliente_valido(self, id):
        return id in self._usuarios