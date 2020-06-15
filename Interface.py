import Empresa
import MysqlConnection
import Cliente


# clase Interface
class Interface:
    connection: MysqlConnection.MysqlConnection
    bd_election: str

    def __init__(self):
        self.empresas = []
        self.empresasCount = len(self.empresas)

    def setEmpresa(self, nombreEmpresa: str, direccionEmpresa: str, rfcEmpresa: str):
        empresa = Empresa.Empresa(str(self.empresasCount),nombreEmpresa,direccionEmpresa,rfcEmpresa)
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
            self.empresas.append(Empresa.Empresa(empresa[0],empresa[1],empresa[2],empresa[3]))

            _clientes = self.connection.fetch_clientes_empresa(empresa[0])

            for cliente in _clientes:

                print(cliente)
                self.empresas[i].setCliente(Cliente.Cliente(cliente[0],cliente[1],cliente[2],cliente[3]))

            i += 1

        self.empresasCount = len(self.empresas)

    def getEmpresa(self,id:str):

        pass

    def getEmpresas(self):

        self.refreshEmpresas()

        return self.empresas

    def setDBElection(self, election: str):

        self.bd_election = election

    def __startConnection(self):

            self.connection = MysqlConnection.MysqlConnection.get_instance()

