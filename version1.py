import json


def priceof(type):
    dealType = 1
    prices = {
        'manta':100
        ,'zarbiya':15
        ,'tlamt':60
    }
    specialPrices = {
        'manta':80
        ,'zarbiya':12,
        'tlamt':50
    }
    def getPrice(type,dealType):
        if dealType == 1:
            return prices[type]
        return specialPrices[type]
    if type == "manta":
        return getPrice(type,dealType)
    if type == "zarbiya":
        x,y = input("x,y=").split(',')
        x,y = int(x),int(y)
        return x*y*getPrice(type,dealType)
    if type == "tlamt":
        x = int(input("x = "))
        return x*getPrice(type,dealType)
class Service:
    def __init__(self,n,clientId) -> None:
        self.id = self.newIdService()
        self.clientId = clientId
        self.n = n
        self.products = []
    def newIdService(self):
        return 1
    def addProduct(self,product):
        if len(self.products) > self.n:
            pass
        self.products.append(product.id)
        return True
    def incrementN(self,k = 1):
        self.n += k

    def deleteProduct(self,id):
        i = 0
        for p in self.products:
            if p == id:
                del self.products[i]
            i += 1
        del self.products[id]
class serviceManager:
    def __init__(self, manager, path="serviceData.json"):
        self.path = path
        self.manager = manager
        manager.Smanager = self
        self.servicesData = {}

    def createService(self, clientId, n):
        service = self.retrieveService(clientId, n, self.getNewId())
        return service

    def getNewId(self):
        id = 1
        while id in self.servicesData.keys():
            id += 1
        return id

    def retrieveService(self, clientId, n, id):
        service = Service(n, clientId)
        service.id = id
        self.addService(service)
        return service

    def addService(self, service):
        self.servicesData[service.id] = service

    def getJsonData(self):
        jsonData = {}
        for id, serv in self.servicesData.items():
            jsonData[id] = {
                'id' : serv.id ,
                "clientId": serv.clientId,
                "n": serv.n,
                "products": serv.products
            }
        return jsonData

    def saveJson(self, targetPath="serviceData.json"):
        path = targetPath
        if targetPath != self.path:
            path = targetPath
            self.lastPath = path
        with open(path, "w") as file:
            json.dump(self.getJsonData(), file)

    def loadJson(self, targetPath="serviceData.json"):
        path = targetPath
        try:
            with open(path, "r") as file:
                data = dict(json.load(file))
                
                service=service.emptyservice()
                service.id= data["id"]
                service.clientId= data["clienId"]
                service.n=data["n"]
                service.products=data["products"]
                self.addService(service)
            return True
        except Exception as e:
            return False

    def push(self):
        serviceManager(self, "servicesData2.json").saveJson("servicesData2.json")
        self.saveJson()
    
    def calculatePrice(self,service):
        price=0
        for id in service.products:
            prod = self.manager.getProduct(id)
            price += prod.price 
            if prod.price == 0:
                print("yoo")


class Product : 
    def __init__(self,type,serviceid) -> None:
        self.type=type
        self.serviceid = serviceid
        self.id = -1
        self.price=0
        self.info = ""
    def getPrice(self):
        price=priceof(self.type)
        return price
    def __json__(self) :
        dic={}
        dic["type"]= self.type
        dic["serviceid"]=self.serviceid
        dic["id"]=self.id
        dic["price"]=self.price
        dic["info"]=self.info

        return dic
    @classmethod
    def emptyProduct(cls):
        p = Product('',0)
        return p

class productManager :
    def __init__(self,manager,path="productData.json") -> None:
        self.path =path 
        self.manager=manager
        manager.Pmanager=self
        self.productsData = {

        }
        self.loadJson()
    def createProduct(self,type,serviceId):
        p = self.retrieveProduct(type,serviceId,self.getNewId())
        return p
    def getNewId(self):
        id= 1 
        while id in self.productsData.keys():
            id+=1 

        return id
    def retrieveProduct(self,type,serviceId,id):
        p = Product(type,serviceId)
        p.id=id
        self.addProduct(p)

        return p
    def addProduct(self,product):
        self.productsData[product.id] = product
    def getJsonData(self):
        jsonData = {}
        for id,prod in self.productsData.items():
            jsonData[id] = prod.__json__()
        return jsonData
    def saveJson(self,targetPath="productData.json"):
        path = targetPath
        if targetPath != self.path:
            path = targetPath
            self.lastPath = path
        with open(path,"w") as file:
            json.dump(self.getJsonData(),file)
    def loadJson(self,targetPath="productData.json"):
        path = targetPath
        try:
            with open(path,"r") as file:
                data = dict(json.load(file))
                for productDict in data.values():
                    product = Product.emptyProduct()
                    for attribute, value in productDict.items():
                        product.__setattr__(attribute,value)
                    self.addProduct(product)
            return True
        except Exception as e:
            return False
    def push(self):
        productManager(self,"productsData2.json").saveJson("productsData2.json")
        self.saveJson()

class Manager:
    def __init__(self) -> None:
        self.Pmanager = None
        self.Smanager = None

manager = Manager()
prodmanager=productManager(manager)
print(prodmanager.productsData)
p0 =prodmanager.createProduct("zarbiya",1)
prodmanager.push()
servManager = serviceManager(manager)
servManager.createService(1,4).addProduct(p0)
servManager.push()
print(priceof('zarbiya'))

        


