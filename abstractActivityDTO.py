class AbstractActivity():
    def __init__(self, name, activityType, inputRelations, outputRelations, implementedBy):
        self.name               = name
        self.activityType     = activityType
        self.inputRelations      = inputRelations
        self.outputRelations     = outputRelations
        self.implementedBy      = implementedBy
    
    # set 
    def setName(self, name):
        self.name = name
    
    def setActivityType(self, activityType):
        self.activityType = activityType
    
    def setInputRelations(self, inputRelations):
        self.inputRelations = inputRelations
    
    def setOutputRelations(self, outputRelations):
        self.outputRelations = outputRelations
    
    def setImplementedBy(self, implementedBy):
        self.implementedBy = implementedBy
    

    # get
    def getName(self):
        return self.name
    
    def getActivityType(self):
        return self.activityType
    
    def getInputRelations(self):
        return self.inputRelations
    
    def getOutputRelations(self):
        return self.outputRelations
    
    def getImplementedBy(self):
        return self.implementedBy
    
    
    
    