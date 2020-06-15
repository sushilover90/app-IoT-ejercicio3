import Empresa
import mysql.connector
from mysql.connector.fabric.connection import MySQLFabricConnection
import Cliente
import Empresa
import Producto


class MysqlConnection:
    __instance__ = None
    _connection: mysql.connector = None
    _cursor: MySQLFabricConnection

    def __init__(self):
        """ Constructor.
       """
        if MysqlConnection.__instance__ is None:
            MysqlConnection.__instance__ = self
        else:
            raise Exception("You cannot create another MysqlConnection class")

    @staticmethod
    def get_instance():
        """ Static method to fetch the current instance.
       """
        if not MysqlConnection.__instance__:
            MysqlConnection()
        return MysqlConnection.__instance__

    def __set_connection(self):
        # host = the database server ip address
        # user = the database user
        # passwd = the database user password
        # database = the database/schema name
        self._connection = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='',
            database='ejercicio3'
        )

    def __close_connection(self, cursor: MySQLFabricConnection):

        if self._connection.is_connected():
            self._connection.close()
            cursor.close()

    def fetch_empresas(self) -> list:

        self.__set_connection()

        cursor = self._connection.cursor()

        sql_select_query_empresas = "select * from Empresa"

        cursor.execute(sql_select_query_empresas)

        empresas = cursor.fetchall()

        self.__close_connection(cursor)

        return empresas

    def fetch_clientes_empresa(self, id_empresa: str) -> list:

        self.__set_connection()

        cursor = self._connection.cursor()

        sql_select_query_clientes_empresa = f'select c.id,c.nombre,c.direccion,c.rfc from cliente c ' \
                                            f'join empresa e on e.id = c.empresa ' \
                                            f'where e.id = {id_empresa}'

        cursor.execute(sql_select_query_clientes_empresa)

        clientes = cursor.fetchall()

        self.__close_connection(cursor)

        return clientes

    def fetch_registered_empresa(self, id_empresa: str) -> list:

        self.__set_connection()

        cursor = self._connection.cursor()

        sql_select_query_last_empresa = f'SELECT * FROM empresa where id = {id_empresa}'

        cursor.execute(sql_select_query_last_empresa)

        empresa = cursor.fetchall()

        self.__close_connection(cursor)

        return empresa

    def fetch_productos(self)->list:

        self.__set_connection()

        cursor = self._connection.cursor()

        sql_select_query_producto = 'select * from producto'

        cursor.execute(sql_select_query_producto)

        productos = cursor.fetchall()

        self.__close_connection(cursor)

        return productos

    def insert_empresa(self, empresa: Empresa.Empresa):

        self.__set_connection()

        cursor = self._connection.cursor()

        sql_insert_query_empresa = f'insert into empresa (nombre,direccion,rfc) ' \
                                   f'values ("{empresa.get_nombre()}","{empresa.get_direccion()}","{empresa.get_nombre()}")'

        cursor.execute(sql_insert_query_empresa)

        self._connection.commit()

        self.__close_connection(cursor)

    def insert_cliente_empresa(self,id_empresa,cliente:Cliente.Cliente):


        self.__set_connection()

        cursor = self._connection.cursor()

        sql_insert_cliente = f'insert into cliente (empresa,nombre,direccion,rfc) ' \
                             f'values ({int(id_empresa)},"{cliente.getNombre()}","{cliente.getDireccion()}", ' \
                             f'"{cliente.getRfc()}")'

        cursor.execute(sql_insert_cliente)

        self._connection.commit()

        self.__close_connection(cursor)

    def insert_producto(self,producto:Producto.Producto):

        self.__set_connection()

        cursor = self._connection.cursor()

        sql_insert_producto = f'insert into producto (nombre,precio_base) ' \
                              f'values ("{producto.get_nombre()}",{producto.get_precio_base()})'

        cursor.execute(sql_insert_producto)

        self._connection.commit()

        self.__close_connection(cursor)