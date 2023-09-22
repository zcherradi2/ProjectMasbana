from datetime import datetime

from subService import SubService


class Service:
    def __init__(self,id,price,date,clientId,isDone=False,serviceDict= {}) -> None:
        self.isDone = False
        self.id = id
        self.price = price
        self.__date = date
        self.clientId = clientId
        self.serviceDict = {}
    def addSubService(self,subservice):
        self.serviceDict[subservice.id] = subservice
    def getNewSubId(self):
        return len(self.serviceDict.values())
    def createSubService(self,type,price):
        id = len(self.serviceDict)
        subService= SubService(id,type,price)
        self.addSubService(subService)
    def setDate(self,newDate):
        try:
            if type(newDate) ==type({}):
                self.__date = datetime(**newDate)
            else:
                self.__date = newDate
        except:
            pass
    def getDate(self):
        return self.__date
    date = property(getDate,setDate)
    def __str__(self) -> str:
        return str(self.id)+","+str(self.price)+","+str(self.date)+", finished: "+str(self.isDone)
    def finished(self):
        self.isDone = True
    @classmethod
    def emptyService(cls):
        return Service(0,0,datetime.min,0)
    def __json__(self):
        resDict = {}
        for att , val in self.__dict__.items():
            #if att not in ["date","__date","serviceDict"]:
            if type(val) != type(datetime.now()):
                resDict[att] = val
        dt = self.date
        resDict["date"] = {"year": str(dt.year), "month": str(dt.month), "day": str(dt.day), "hour": str(dt.hour), "minute": str(dt.minute), "second": str(dt.second)}
        serviceDict = self.serviceDict
        for id, subService in serviceDict.items():
            serviceDict[id] = subService.__dict__
        resDict["serviceDict"] = serviceDict
        return resDict
    