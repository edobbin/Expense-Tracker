
class asset:
    def __init__(self, name, desc, price, ID):
        self.name =name
        self.desc = desc
        self.price = price
        self.ID = ID

    def getName(self):
        return str(self.name)
    def setName(self,name):
        self.name = name

    def getDesc(self):
        return self.desc
    def setDesc(self,desc):
        self.desc = desc
    
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price = price
    
    def getID(self):
        return str(self.ID)
    
    def __str__(self) -> str:
        return "Name: "+str(self.name)+" ID:"+str(self.ID)
        
    