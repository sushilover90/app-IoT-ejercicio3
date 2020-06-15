import Empresa
import mysql.connector
from mysql.connector.fabric.connection import MySQLFabricConnection
import Cliente
import Empresa


class MysqlConnection:
    __instance__ = None
    _connection: mysql.connector = None
    _cursor:MySQLFabricConnection

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

    def __close_connection(self,cursor:MySQLFabricConnection):

        if self._connection.is_connected():
            self._connection.close()
            cursor.close()

    def fetch_empresas(self)->list:

        self.__set_connection()

        cursor = self._connection.cursor()

        sql_select_query_empresas = "select * from Empresa"

        cursor.execute(sql_select_query_empresas)

        empresas = cursor.fetchall()

        self.__close_connection(cursor)

        return empresas

    def fetch_clientes_empresa(self,id_empresa:str)->list:

        self.__set_connection()

        cursor = self._connection.cursor()

        sql_select_query_clientes_empresa = f'select c.id,c.nombre,c.direccion,c.rfc from empresa_cliente ec ' \
                                            f'join empresa e on ec.empresa = e.id ' \
                                            f'join cliente c on ec.cliente = c.id where e.id = {id_empresa}'

        cursor.execute(sql_select_query_clientes_empresa)

        clientes = cursor.fetchall()

        self.__close_connection(cursor)

        return clientes
