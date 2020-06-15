import Empresa
import MysqlConnection
import Cliente
import Producto


# clase Interface
class Interface:
    connection: MysqlConnection.MysqlConnection

    def __init__(self):
        self.empresas = []
        self.empresasCount = len(self.empresas)
        self.clientes = []
        self.productos = []

    def get_empresa_index(self) -> int:
        return self.empresasCount

    def get_last_empresa(self) -> Empresa.Empresa:
        return self.empresas[self.get_empresa_index()]

    # agregando empresa
    def add_empresa(self, nombreEmpresa: str, direccionEmpresa: str, rfcEmpresa: str):

        self.__startConnection()

        empresa = Empresa.Empresa(nombreEmpresa, direccionEmpresa, rfcEmpresa)

        self.connection.insert_empresa(empresa)

        self.empresas.append(empresa)

    def add_producto(self, nombre_producto:str, precio_base:float):

        self.__startConnection()

        producto = Producto.Producto(nombre_producto,precio_base)

        self.connection.insert_producto(producto)

    # fetch empresas de la bd (mysql)
    def refresh_empresas(self):

        self.__startConnection()

        _empresas = self.connection.fetch_empresas()

        # refresh lista empresas
        self.empresas.clear()

        i = 0
        for empresa in _empresas:

            # [0] = id
            # [1] = nombre
            # [2] = direccion
            # [3] = rfc
            self.empresas.append(Empresa.Empresa(empresa[1], empresa[2], empresa[3],empresa[0]))

            _clientes = self.connection.fetch_clientes_empresa(empresa[0])

            for cliente in _clientes:
                self.empresas[i].set_cliente(Cliente.Cliente(cliente[1], cliente[2], cliente[3], cliente[0]))

            i += 1

        self.empresasCount = len(self.empresas)

    def prepare_list_clientes(self, cliente: Cliente.Cliente):

        self.clientes.append(cliente)

    def get_list_clientes_length(self) -> int:

        return len(self.clientes)

    def get_empresa(self, id: str):

        pass

    def get_empresas(self):

        self.refresh_empresas()

        return self.empresas

    def get_productos(self):

        self.refresh_productos()

        return self.productos

    def __startConnection(self):

        self.connection = MysqlConnection.MysqlConnection.get_instance()

    def refresh_productos(self):

        self.__startConnection()

        productos = self.connection.fetch_productos()

        self.productos.clear()

        for producto in productos:
            # [0] id
            # [1] nombre
            # [2] precio_base
            self.productos.append(Producto.Producto(producto[1], float(producto[2]), producto[0]))

    def get_cliente_instance(self, nombre_cliente: str, direccion_cliente: str, rfc_cliente: str,
                             _id: str = None) -> Cliente.Cliente:

        return Cliente.Cliente(nombre_cliente, direccion_cliente, rfc_cliente, _id)
