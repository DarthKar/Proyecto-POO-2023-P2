class ChoppeException(Exception):
    def __init__(self, mensaje_error):
        self.mensaje_error = mensaje_error

    def get_mensaje(self):
        return self.mensaje_error


class BaseDatosError(ChoppeException):
    def __init__(self, mensaje_error) -> None:
        super().__init__(mensaje_error)


class CompraError(ChoppeException):
    def __init__(self, mensaje_error) -> None:
        super().__init__(mensaje_error)

class InventarioCompraError(CompraError):
    def __init__(self, mensaje_error) -> None:
        super().__init__(mensaje_error)

class ProductoError(CompraError):
    def __init__(self, mensaje_error) -> None:
        super().__init__(mensaje_error)

class ValidacionCompraError(CompraError):
    def __init__(self, mensaje_error) -> None:
        super().__init__(mensaje_error)

class DevolucionError(ChoppeException):
    def __init__(self, mensaje_error) -> None:
        super().__init__(mensaje_error)

class OrdenError(DevolucionError):
    def __init__(self, mensaje_error) -> None:
        super().__init__(mensaje_error)

class ValidacionDevolucionError(DevolucionError):
    def __init__(self, mensaje_error) -> None:
        super().__init__(mensaje_error)

class InventarioDevolucionError(DevolucionError):
    def __init__(self, mensaje_error) -> None:
        super().__init__(mensaje_error)