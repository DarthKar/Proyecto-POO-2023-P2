import main 
import base_datos as bd

class Opinion(main):
    def __init__(self, comentario, valoracion):
        self.comentario = comentario
        self.valoracion = valoracion


    bdp = bd.getProductos()
    bdc = bd.getCompradores()
    bdv = bd.getVendedores()   

    def crear_opinion(self, creador, objeto, comentario, valoracion):
        
        return "Opinión creada con éxito"

    def editar_opinion(self, creador, objeto, comentario, valoracion):
        # Implementa la lógica de edición de la opinión aquí
        return "Opinión editada con éxito"

    def borrar_opinion(self, creador, objeto):
        # Implementa la lógica de borrado de la opinión aquí
        return "Opinión borrada con éxito"
