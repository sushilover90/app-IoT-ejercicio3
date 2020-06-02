import Empresa


# clase Interfaz
class Interfaz:
    def __init__(self):
        self.empresas = []
        self.empresasCount = len(self.empresas)

    def setEmpresa(self,nombreEmpresa : str,direccionEmpresa : str,rfcEmpresa: str):

        empresa = Empresa.Empresa(nombreEmpresa, direccionEmpresa, rfcEmpresa,self.empresasCount)
        self.empresas.append(empresa)

    def getLastEmpresa(self) -> Empresa:
        ultimaEmpresa = self.empresas[self.empresasCount]
        self.empresasCount += 1
        return ultimaEmpresa

    def getEmpresas(self):
        return self.empresas

