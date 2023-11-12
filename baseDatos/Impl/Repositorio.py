import os
import BaseDatos
import pickle

class Repositorio:
    baseDatos=[]
    FILE = "basedatos.txt"
    PATH = os.path.join(os.getcwd(), "temp", "{}")

    
    @classmethod
    def leer(cls):
        if cls.crearDirectorio() or cls.crearArchivo():
            global baseDatos
            baseDatos=BaseDatos()
            cls.guardarArchivo()
            return
    leer()
    @classmethod
    def guardarArchivo(cls):
        try:
             with open(cls.PATH,"wb") as archivo:
                  pickle.dump(baseDatos,archivo)
        except Exception as e:
             raise RuntimeError(e)
    @classmethod
    def crearArchivo(cls):
        return not os.path.exists(os.path.join(cls.PATH.format(cls.FILE)))
    @classmethod
    def crear_directorio(cls):
        try:
            path = os.path.join(cls.PATH.format(""))
            if os.path.exists(path):
                return False
            os.makedirs(path)
            return True
        except Exception as e:
            raise RuntimeError(e)