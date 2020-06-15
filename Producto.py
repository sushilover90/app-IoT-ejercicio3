class Producto:

    def __init__(self, nombre: str, precio_base: float, id: str = None):
        self.nombre = nombre
        self.precio_base = precio_base
        self.id = id

    def get_id(self) -> str:
        return self.id

    def get_nombre(self) -> str:
        return self.nombre

    def get_precio_base(self) -> float:
        return self.precio_base
