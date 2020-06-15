import Interface
import Cliente
import Empresa


# clase Menu
class Menu:
    def __init__(self):
        self.stop = False
        self.interface = Interface.Interface()

    def agregarEmpresa(self):

        nombreEmpresa = input('Ingrese el nombre de la empresa:\n').upper()
        direccionEmpresa = input('Ingrese la dirección de la empresa:\n').upper()
        rfcEmpresa = input('Ingrese el rfc de la empresa:\n').upper()

        self.interface.setEmpresa(str(self.interface.getEmpresaIndex() + 1), nombreEmpresa, direccionEmpresa,
                                  rfcEmpresa)

        ultimaEmpresa = self.interface.getLastEmpresa()

        print(f'''

        Se agrego la empresa: {ultimaEmpresa.getNombre()}
        con direccion: {ultimaEmpresa.getDireccion()}
        RFC: {ultimaEmpresa.getRfc()}

        ''')

        self.agregarClientesEmpresa(ultimaEmpresa)

    def agregarClientesEmpresa(self, empresaAgregarClientes: Empresa.Empresa = None, id_empresa=None):

        stopLlenadoClientes = False
        print('Proceda a ingresar los clientes')
        clientesIngresados = 0

        if empresaAgregarClientes is not None:
            _id_empresa = empresaAgregarClientes.getId()

        if id_empresa is not None:
            _id_empresa = id_empresa

        while not stopLlenadoClientes:
            cancelar = False

            if clientesIngresados > 0:

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
                cliente = Cliente.Cliente(nombreCliente, direccionCliente, rfcCliente)

                self.interface.connection.insert_cliente_empresa(_id_empresa, cliente)

                print(f'''
                Se ingresó al cliente:

                {cliente.getDatos()}

                ''')

                clientesIngresados += 1

    def setOperacion(self):
        _input = input()

        if _input.upper() == '1':
            self.agregarEmpresa()


        elif _input.upper() == '2':

            self.describeEmpresas(True)

        elif _input.upper() == '3':

            self.describeEmpresas(False)
            _input = input().upper()
            self.agregarClientesEmpresa(None,_input)

        elif _input.upper() == '4':
            self.stop = True
            print('Adios')

    def getMenu(self):
        print('''
            ¿Qué desea hacer? Ingrese el numero para
            1) Agregar empresa
            2) Imprimir empresas
            3) Agregar cliente a una empresa
            4) Salir
        ''')

    def describeEmpresas(self, showClientes: bool):

        if len(self.interface.getEmpresas()) > 0:

            if not showClientes:

                print('¿A qué empresa desea agregar? '
                      'Eliga su id\n')

            for empresa in self.interface.getEmpresas():

                print(f'\nId: {empresa.getId()}'
                      f'\nEmpresa: {empresa.nombre}. '
                      f'\nDireccion: {empresa.direccion}.')

                if showClientes:

                    print(f'Clientes:')
                    for cliente in empresa.clientes:
                        print(f'''
                            \n{cliente.getDatos()}\n
                        ''')

        else:
            print('No hay empresas registradas. Regístre una/varias empresa(s) antes de visualizarla(s).')

    def run(self):
        while not self.stop:
            self.getMenu()
            self.setOperacion()
