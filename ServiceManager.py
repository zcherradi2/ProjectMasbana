import json
from Service import Service
from datetime import datetime
from subService import SubService
class ServiceManager:
    def __init__(self,services=[],path="serviceData.json") -> None:
        self.data = {}
        self.path = path
        self.lastPath = path
        self.addServices(services)
        self.successLoading = self.loadJson()
    def addService(self,service):
        self.data[service.id] = service
    def findServiceById(self,id):
        try:
            return self.data[id]
        except:
            return None
    def addServices(self,services):
        for service in services:
            self.addService(service)
    def getSpecialId(self,id):
        while id in self.data.keys():
            id += 1
        return id
    def createService(self,price,clientId):
        id = len(self.data.values())+1
        if id in self.data.keys():
            id = self.getSpecialId(id)
        service = Service(id,price,datetime.now(),clientId)
        self.addService(service)
        return service
    def getJsonData(self):
        jsonData = {}
        for id,service in self.data.items():
            jsonData[id] = service.__json__()
        return jsonData
    def normalize(self,dic):
        res = {}
        for key,val in dic.items():
            res[key] = int(val)
        return res
    def saveJson(self,targetPath="serviceData.json"):
        #if not self.successLoading:
        #    return
        path = targetPath
        if targetPath != self.path:
            path = targetPath
            self.lastPath = path
        with open(path,"w") as file:
            json.dump(self.getJsonData(),file)
    def loadJson(self,targetPath="serviceData.json"):
        path = targetPath
        try:
            
            with open(path,"r") as file:
                data = dict(json.load(file))
                for serviceDict in data.values():
                    if dict(serviceDict)=={}:
                        continue
                    service = Service.emptyService()
                    for attribute, value in serviceDict.items():
                        if attribute == "date":
                            dateDict = self.normalize(dict(value))
                            service.__setattr__(attribute, datetime(**dateDict))
                        elif attribute =="id":
                            service.id = int(value)
                        elif attribute == "serviceDict":
                            sserviceDict = dict(value)
                            if len(sserviceDict)!=0:
                                for id, subService in sserviceDict.items():
                                    sserviceDict[id] = SubService(**subService)
                                service.serviceDict = sserviceDict
                            else:
                                service.serviceDict = {}
                        else:
                            service.__setattr__(attribute,value)
                    self.addService(service)
            return True
        except Exception as e:
            print(e)
            return False
    def findServicesByClientId(self,clientId):
        services = []
        for service in self.data.values():
            if service.clientId == clientId:
                services.append(service)
        return services

"""sManager = ServiceManager()
service1 = sManager.createService(1000,1)
service2 = sManager.createService(2000,1)
service3 = sManager.createService(150,2)
sManager.createService(165,1)
sManager.saveJson()
print(sManager.data)"""
