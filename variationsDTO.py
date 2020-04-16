class Variation():
    def __init__(self, name, abstract_activity):
        self.name               = name
        self.abstract_activity  = abstract_activity
        
    
    # set 
    def setName(self, name):
        self.name = name
    
    def setAbstractActivityt(self, abstract_activity):
        self.abstract_activity = abstract_activity
    

    # get
    def getName(self):
        return self.name
    
    def getAbstractActivity(self):
        return self.abstract_activity