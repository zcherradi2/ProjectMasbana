from ServiceManager import ServiceManager
from ClientManager import ClientManager
serviceManager = ServiceManager()
clientManager = ClientManager()

def delevary(input):
    if(input == "yes"):
        return True
    return False
def importt(input):
    if(input=="yes"):
        return True
    return False
def calcPrice(imported,serviceHeight,serviceWidth,type):
    return 100
def addService(imported,clientId):
    #serviceHeight = float(input("height:"))
    #serviceWidth = float(input("width:"))
    #type = input("type of service")
    #price = calcPrice(imported,serviceHeight,serviceWidth,type)
    service = serviceManager.createService(0,clientId)
    print(service.id)
def addNewServices():
            imported = importt(input("import?"))
            #delev = delevary(input("with delevary?"))
            name = input("clientName :")
            clientPhone = input("client phone")
            email = input("client email:")
            adress = input("client adress:")
            client = clientManager.createClient(name,"",clientPhone,adress,email)
            #numServices = int(input("the number of services"))
            #for i in range(numServices):
                #print("service "+str(i+1))
                #addService(imported,client.id)
            addService(imported,client.id)
            clientManager.saveJson()
            serviceManager.saveJson()
def checkService():
    id = int(input("the id of the service"))
    service = serviceManager.findServiceById(id)
    clientId = service.clientId
    client = clientManager.findById(clientId)
    if service != None:
        print(service)
        print(client)
    else:
        print("no service with this id was found")
def checkClientServices():
    clientId = int(input("client id"))
    services = serviceManager.findServicesByClientId(clientId)
    if len(services) != 0:
        for service in services:
            print(service)
    else:
        print("client doesn't exist")


while True:
    try:
        print("-type 'a' to add new services")
        print("-type 'check service' to check a service")
        print("-type '3' to check client services")
        print("- type q to quit")
        choice = input("make your choice:")
        if choice == 'a':
            addNewServices()
        if choice == "check service":
            checkService()
        if choice == "3":
            checkClientServices()
        if choice =="q":
            break
        print(serviceManager.findServiceById(1).serviceDict)
    except Exception as e:
        print(e)




    