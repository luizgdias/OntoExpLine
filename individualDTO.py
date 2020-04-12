class Individual():
    def __init__(self, name, comment, is_a, seeAlso, individuals):
        self.name               = name
        self.comment            = ''.join(comment)
        self.is_a               = is_a
        self.seeAlso            = seeAlso
        self.individuals        = individuals
    
    # set 
    def setName(self, name):
        self.name = name
    
    def setComment(self, comment):
        self.comment = comment
    
    def setPropertiesRange(self, is_a):
        self.is_a = is_a
    
    def setSeeAlso(self, seeAlso):
        self.seeAlso = seeAlso
    
    def setIndividuals(self, individuals):
        self.individuals = individuals

    # get
    def getName(self):
        return self.name
    
    def getComment(self):
        return self.comment
    
    def getIs_a(self):
        return self.is_a
    
    def getSeeAlso(self):
        return self.seeAlso
    
    def getIndividuals(self):
        return self.individuals
    
    
    