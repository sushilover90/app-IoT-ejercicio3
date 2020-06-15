import Cliente

# clase empresa
class Empresa:

    # constructor
    def __init__(self,nombre:str,direccion:str,rfc:str,id:str = None):
        self.clientes = []
        self.nombre = nombre
        self.direccion = direccion
        self.rfc = rfc
        self.id = id

    def get_id(self):
        return self.id

    # traer los clientes de la instancia de la empresa
    def get_clientes(self):
        return self.clientes

    # traer el nombre de la empresa
    def get_nombre(self):
        return self.nombre

    # traer la dirección de la empresa
    def get_direccion(self):
        return self.direccion

    # traer el rfc de la empresa
    def get_rfc(self):
        return self.rfc

    # set (agregar) cliente a la empresa
    def set_cliente(self, cliente):
        self.clientes.append(cliente)

    def get_cantidad_clientes(self) -> int:
        return len(self.clientes)

    def refresh_clientes(self, clientes:[]):

        self.clientes.clear()

        self.clientes = clientes