# clase Cliente
class Cliente:
    def __init__(self,nombre:str,direccion:str,rfc:str,id:str = None):
        self.id = id
        self.nombre = nombre
        self.direccion = direccion
        self.rfc = rfc

    def getNombre(self):
        return self.nombre

    def getDireccion(self):
        return self.direccion

    def getRfc(self):
        return self.rfc

    def getDatos(self):
        return f'\tId cliente: {self.id}\n' \
               f'\tNombre cliente: {self.nombre}\n' \
               f'\tDireccion cliente: {self.direccion}\n' \
               f'\tRFC  cliente: {self.rfc}'
