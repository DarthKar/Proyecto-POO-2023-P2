class Usuario:
    def __init__(self,id,nombre,apellido,correo):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo

        def getId(self):
            return self.id
        
        def setId(self,id):
            self.id = id
        
        def getNombre(self):
            return self.nombre

        def setNombre(self,nombre):
            self.nombre = nombre
        
        def getApellido(self):
            return self.apellido
        
        def getNombreCompleto(self):
            return self.nombre+" "+self.apellido
        
        def setApellido(self,apellido):
            self.apellido = apellido
        
        def getCorreo(self):
            return self.correo
        
        def setCorreo(self,correo):
            self.correo = correo