class income:

    def __init__(self, name, desc, price, date) -> None:
        self.name = name
        self.desc = desc
        self.price = price
        self.date = date

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
    def setCost(self,price):
        self.price = price
    
    def getID(self):
        return str(self.ID)
    def getDate(self):
        return str(self.date)