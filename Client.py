class Client:
    def __init__(self,id,name,lastname,phoneNumber,adress,email) -> None:
        self.id = id
        self.name = name
        self.lastName = lastname
        self.phoneNumber = phoneNumber
        self.adress = adress
        self.email = email
    def setFullName(self,fullName):
        fullNameWords = fullName.split(" ")
        self.name = fullNameWords[0]
        lastName = ""
        for w in fullNameWords[1:]:
            lastName += w + " "
        lastName = lastName[0:-1]
        self.lastName = lastName
    @classmethod
    def emptyClient(cls):
        return Client(0,"","","","","")
    def sendDone(self):
        pass
    def __str__(self) -> str:
        return str(self.id)+","+self.name+","+self.lastName+","+str(self.phoneNumber)+","+str(self.adress)+","+self.email
    def __json__(self):
        return self.__dict__
cl = Client(1,"zakaria","cherradi","0667451133","mesnana ti7ad","zcherradi@gmail.com")
    