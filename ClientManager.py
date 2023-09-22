import json
from Client import Client
class ClientManager:
    def __init__(self,clients=[],path="data.txt") -> None:
        self.data = {}
        self.path = path
        self.lastPath = self.path

        self.loadJson()
    def getClientList(self):
        return list(self.data.values())
    clientList = property(getClientList)
    def addClient(self,client):
        self.data[client.id] = client
    def addClients(self,clients):
        for client in clients:
            self.addClient(client)
    def getSpecialId(self,id):
        while id in self.data.keys():
            id += 1
        return id
    def createClient(self,name,lastName,phoneNumber,adress,email):
        id = len(self.data.values())+1
        if id in self.data.keys():
            id = self.getSpecialId(id)
        client = Client(id,name,lastName,phoneNumber,adress,email)
        self.addClient(client)
        return client
    def retrieveClient(self,clientInfo):
        clientAttributs = clientInfo.split(",")
        id = int(clientAttributs[0])
        name = clientAttributs[1]
        lastName = clientAttributs[2]
        phone = clientAttributs[3]
        adress = clientAttributs[4]
        email = clientAttributs[5]
        client = Client(id,name,lastName,phone,adress,email)
        return client
    def saveData(self,targetPath="data.txt"):
        path = self.path
        if targetPath != self.path:
            path = targetPath
            self.lastPath = path
        with open(path,"w") as file:
            for client in self.data.values():
                file.write(str(client)+"\n")
    def loadData(self,targetPath="data.txt"):
        path = self.lastPath
        if targetPath != self.lastPath:
            path = targetPath
        try:
            with open(path,"r") as file:
                for line in file:
                    n = len(line)
                    clientInfo = line[0:n-1]
                    client = self.retrieveClient(clientInfo)
                    self.addClient(client)
            return True
        except Exception as e:
            return False
    def getJsonData(self):
        jsonData = {}
        for id,client in self.data.items():
            jsonData[id] = client.__json__()
        return jsonData
    def saveJson(self,targetPath="data.json"):
        path = targetPath
        if targetPath != self.path:
            path = targetPath
            self.lastPath = path
        with open(path,"w") as file:
            json.dump(self.getJsonData(),file)
    def loadJson(self,targetPath="data.json"):
        path = targetPath
        try:
            with open(path,"r") as file:
                data = dict(json.load(file))
                for clientDict in data.values():
                    client = Client.emptyClient()
                    for attribute, value in clientDict.items():
                        client.__setattr__(attribute,value)
                    self.addClient(client)
            return True
        except Exception as e:
            return False
    def findById(self,id):
        try:
            return self.data[id]
        except:
            return None










clientManager = ClientManager()
clientManager.createClient("zakaria","cheradg","0046315","adsad","zcherra@gma.com")
clientManager.createClient("sdfsd","cheradg","454","adsad","zcherra@gma.com")
clientManager.createClient("gtr","cheradg","0046315","adsad","zcherra@gma.com")
clientManager.createClient("rwe","cheradg","0046315","adsad","zcherra@gma.com")
#clientManager.saveData()
#result = clientManager.loadData()
clientManager.saveJson()

