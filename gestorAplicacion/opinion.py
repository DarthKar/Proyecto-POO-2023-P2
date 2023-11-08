class opinion:
    
    def __init__(self, opinion, valoracion, creador=None):
        self.opinion = opinion
        self.valoracion= valoracion
        self.creador = creador

    def getOpinion(self):
        return self.opinion
    def setOpinion(self, op):
         self.opinion = op 
    
    
        


