class ChoppeException(Exception):
    def __init__(self, mensaje_error):
        self.mensaje_error = mensaje_error

    def get_mensaje(self):
        return self.mensaje_error

class BaseDatosError(ChoppeException):
    def __init__(self, mensaje_error) -> None:
        super().__init__(mensaje_error)

