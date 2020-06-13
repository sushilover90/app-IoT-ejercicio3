import Interface
import Cliente

# clase Menu
class Menu:
    def __init__(self):
        self.stop = False
        self.interface = Interface.Interface()

    def agregarEmpresa(self):
        nombreEmpresa = input('Ingrese el nombre de la empresa:\n').upper()
        direccionEmpresa = input('Ingrese la dirección de la empresa:\n').upper()
        rfcEmpresa = input('Ingrese el rfc de la empresa:\n').upper()

        self.interface.setEmpresa(nombreEmpresa, direccionEmpresa, rfcEmpresa)
        ultimaEmpresa = self.interface.getLastEmpresa()

        print(f'''

        Se agrego la empresa: {ultimaEmpresa.getNombre()}
        con direccion: {ultimaEmpresa.getDireccion()}
        RFC: {ultimaEmpresa.getRfc()}

        ''')

        self.agregarClientesEmpresa(ultimaEmpresa)

    def agregarClientesEmpresa(self, empresaAgregarClientes):

        stopLlenadoClientes = False
        empresa = empresaAgregarClientes
        print('Proceda a ingresar los clientes')

        while not stopLlenadoClientes:
            cancelar = False

            if empresa.getCantidadClientes() > 0:

                respuestaCorrecta = False

                while not respuestaCorrecta:
                    _input = input('Desea seguir agregando más clientes(S/N):\n').upper()

                    if _input == 'N':
                        cancelar = True
                        stopLlenadoClientes = True
                        respuestaCorrecta = True
                    elif _input == 'S':
                        respuestaCorrecta = True

            if not cancelar:
                nombreCliente = input('Ingrese el nombre del cliente:\n').upper()
                direccionCliente = input('Ingrese la direccion del cliente:\n').upper()
                rfcCliente = input('Ingrese el rfc del cliente:\n').upper()
                cliente = Cliente.Cliente(nombreCliente,direccionCliente,rfcCliente)
                empresa.setCliente(cliente)
                print(f'''
                Se ingresó al cliente:

                {cliente.getDatos()}

                ''')

    def setOperacion(self):
        _input = input()

        if _input.upper() == '1':
            self.agregarEmpresa()


        elif _input.upper() == '2':

            if len(self.interface.getEmpresas()) > 0:
                for empresa in self.interface.getEmpresas():
                    print(f'''
                    Empresa: {empresa.nombre}.
                    Direccion: {empresa.direccion}.
                    Clientes:''')
                    for cliente in empresa.getClientes():
                        print(f'{cliente.getDatos()}')
            else:
                print('No hay empresas registradas. Regístre una/varias empresa(s) antes de visualizarla(s).')

        elif _input.upper() == '3':
            self.stop = True
            print('Adios')

    def getMenu(self):
        print('''
            ¿Qué desea hacer? Ingrese el numero para
            1) Agregar empresa
            2) Imprimir empresas
            3) Salir
        ''')

    def run(self):
        while not self.stop:
            self.getMenu()
            self.setOperacion()

