from abc import ABC, abstractmethod


class ITransaccion(ABC):
    @abstractmethod
    def agregar_producto(self, producto_transaccion):
        pass

    @abstractmethod
    def remover_producto(self, producto_transaccion):
        pass

    @abstractmethod
    def modificar_producto(self, producto_transaccion, cantidad):
        pass