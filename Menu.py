import Interface
import Cliente
import Empresa


# clase Menu
class Menu:
    def __init__(self):
        self.stop = False
        self.interface = Interface.Interface()

    def add_empresa(self):

        nombreEmpresa = input('Ingrese el nombre de la empresa:\n').upper()
        direccionEmpresa = input('Ingrese la dirección de la empresa:\n').upper()
        rfcEmpresa = input('Ingrese el rfc de la empresa:\n').upper()

        self.interface.add_empresa(nombreEmpresa, direccionEmpresa,
                                   rfcEmpresa)

        ultimaEmpresa = self.interface.get_last_empresa()

        print(f'''

        Se agrego la empresa: {ultimaEmpresa.get_nombre()}
        con direccion: {ultimaEmpresa.get_direccion()}
        RFC: {ultimaEmpresa.get_rfc()}

        ''')

        self.add_clientes_empresa(ultimaEmpresa)

    def add_clientes_empresa(self, empresaAgregarClientes: Empresa.Empresa = None, id_empresa=None):

        stopLlenadoClientes = False
        print('Proceda a ingresar los clientes')
        clientesIngresados = 0

        if empresaAgregarClientes is not None:
            _id_empresa = empresaAgregarClientes.get_id()

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
                cliente = self.interface.get_cliente_instance(nombreCliente, direccionCliente, rfcCliente)

                self.interface.connection.insert_cliente_empresa(_id_empresa, cliente)

                print(f'''
                Se ingresó al cliente:

                {cliente.getDatos()}

                ''')

                clientesIngresados += 1

    def add_producto(self):

        stop_llenado_productos = False

        productos_ingresados = 0

        while not stop_llenado_productos:
            cancelar = False

            if productos_ingresados > 0:

                respuestaCorrecta = False

                while not respuestaCorrecta:
                    _input = input('Desea seguir agregando más productos(S/N):\n').upper()

                    if _input == 'N':
                        cancelar = True
                        stop_llenado_productos = True
                        respuestaCorrecta = True
                    elif _input == 'S':
                        respuestaCorrecta = True

            if not cancelar:
                nombre_producto = input('Ingrese el nombre del producto:\n').upper()
                precio_base = input('Ingrese el precio base del producto. Ej: 100.50:\n')
                precio_base.replace('$', '')
                precio_base.replace(',', '.')

                self.interface.add_producto(nombre_producto,float(precio_base))

                print(f'''
                        Se agregó el producto: {nombre_producto} con un precio base de: {precio_base}
                        ''')

                productos_ingresados += 1

    def set_operacion(self):
        _input = input().upper()

        if _input == '1':
            self.add_empresa()

        elif _input == '2':
            self.describe_empresas(True)

        elif _input == '3':
            self.describe_empresas(False)
            _input = input().upper()
            self.add_clientes_empresa(None, _input)

        elif _input == '4':
            self.describe_productos()

        elif _input == '5':
            self.add_producto()

        elif _input == '7':
            self.stop = True
            print('Adios')

        print(_input)

        if _input == '' or _input != '7':
            input('\nPulse cualquier tecla para continuar.\t')

    def get_menu(self):
        print('''
            ¿Qué desea hacer? Ingrese el numero para
            1) Agregar empresa
            2) Imprimir empresas
            3) Agregar cliente a una empresa
            4) Imprimir productos
            5) Agregar producto
            6) Agregar compra
            7) Salir
        ''')

    def describe_empresas(self, showClientes: bool):

        if len(self.interface.get_empresas()) > 0:

            if not showClientes:
                print('¿A qué empresa desea agregar? '
                      'Eliga su id\n')

            for empresa in self.interface.get_empresas():

                print(f'\nId: {empresa.get_id()}'
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

    def describe_productos(self):

        if len(self.interface.get_productos()) > 0:

            print('Productos existentes:')

            for producto in self.interface.get_productos():
                print(f'''
                    Id : {producto.get_id()}
                    Nombre: {producto.get_nombre()}
                    Precio base: {producto.get_precio_base()}''')

        else:
            print('No hay productos registrados. Regístre uno/varios productos(s) antes de visualizarlo(s).')

    def run(self):
        while not self.stop:
            self.get_menu()
            self.set_operacion()
