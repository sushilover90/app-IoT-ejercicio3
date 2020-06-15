import Empresa
import MysqlConnection
import Cliente


# clase Interface
class Interface:
    connection: MysqlConnection.MysqlConnection

    def __init__(self):
        self.empresas = []
        self.empresasCount = len(self.empresas)
        self.clientes = []

    def getEmpresaIndex(self) -> int:
        return self.empresasCount

    def getLastEmpresa(self) -> Empresa.Empresa:
        return self.empresas[self.getEmpresaIndex()]

    # agregando empresa
    def setEmpresa(self, id: str, nombreEmpresa: str, direccionEmpresa: str, rfcEmpresa: str):

        self.__startConnection()

        empresa = Empresa.Empresa(id, nombreEmpresa, direccionEmpresa, rfcEmpresa)

        self.connection.insert_empresa(empresa)

        self.empresas.append(empresa)

    # fetch empresas de la bd (mysql)
    def refreshEmpresas(self):

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
            self.empresas.append(Empresa.Empresa(empresa[0], empresa[1], empresa[2], empresa[3]))

            _clientes = self.connection.fetch_clientes_empresa(empresa[0])

            for cliente in _clientes:
                self.empresas[i].setCliente(Cliente.Cliente(cliente[1], cliente[2], cliente[3],cliente[0]))

            i += 1

        self.empresasCount = len(self.empresas)

    def prepareListClientes(self,cliente:Cliente.Cliente):

        self.clientes.append(cliente)

    def insertClientes(self,id_empresa:str):

        self.__startConnection()

        self.connection.insert_clientes_empresa(id_empresa,self.clientes)

    def getListClientesLength(self)->int:

        return len(self.clientes)

    def getEmpresa(self, id: str):

        pass

    def getEmpresas(self):

        self.refreshEmpresas()

        return self.empresas

    def __startConnection(self):

        self.connection = MysqlConnection.MysqlConnection.get_instance()
