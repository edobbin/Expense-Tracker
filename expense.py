class Expense:
    def __init__(self,name,desc,cost,ID,date) -> None:
        self.name = name
        self.desc = desc
        self.cost = cost 
        self.ID = ID
        self.date = date
    
    def getName(self):
        return str(self.name)
    def setName(self,name):
        self.name = name

    def getDesc(self):
        return self.desc
    def setDesc(self,desc):
        self.desc = desc
    
    def getCost(self):
        return self.cost
    def setCost(self,cost):
        self.cost = cost
    
    def getID(self):
        return str(self.ID)
    def getDate(self):
        return str(self.date)
    