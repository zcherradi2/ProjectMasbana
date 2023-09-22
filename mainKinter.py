import threading
import tkinter
import tkinter.messagebox
import customtkinter
import servicemanager

import subService
from ClientManager import ClientManager
from Service import Service
from ServiceManager import ServiceManager

customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

def lamda(f,parameters):
    def resF(event):
        return f(**parameters)
    return resF

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.client_manager = ClientManager()
        self.service_manager = ServiceManager()
        self.typesPrices = {"zarbiya":100,"gza d n7al":13000,"zama":20}
        self.subServiceType = list(self.typesPrices.keys())
        # configure window
        self.title("CustomTkinter complex_example.py")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure((1,2,3), weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)


        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="tools",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_new_service = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event,
                                                                  text="new Service")
        self.sidebar_button_new_service.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_check_service = customtkinter.CTkButton(self.sidebar_frame,
                                                                    command=self.sidebar_button_event,
                                                                    text="check Service")
        self.sidebar_button_check_service.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_check_client_services = customtkinter.CTkButton(self.sidebar_frame,
                                                                            command=self.sidebar_button_event,
                                                                            text="check client services")
        self.sidebar_button_check_client_services.grid(row=3, column=0, padx=20, pady=10)
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                                       values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame,
                                                               values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        self.tabview = customtkinter.CTkTabview(self, width=250)
        self.tabview.grid(row=0, column=1,columnspan=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
        self.tabview.add("add new service")
        self.tabview.add("check service")
        self.tabview.add("check a client")
        self.tabview.tab("add new service").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
        self.tabview.tab("check service").grid_columnconfigure(0, weight=1)
        self.tabview.tab("check a client").grid_columnconfigure(0, weight=1)
        self.imported_var = customtkinter.Variable(self)
        self.imported_check_button = customtkinter.CTkCheckBox(self.tabview.tab("add new service"),text="imported?",variable=self.imported_var)
        self.imported_check_button.grid(row=0, column=0, padx=20, pady=(5, 10))

        self.add_services_input_frame = customtkinter.CTkFrame(self.tabview.tab("add new service"))
        self.add_services_input_frame.grid_columnconfigure((0, 1), weight=1)
        self.add_services_input_frame.grid(row=1,column=0,rowspan=5,padx=0,pady=0)

        self.create_attr_layout(self.add_services_input_frame,"client_name",row=1)
        self.create_attr_layout(self.add_services_input_frame, "client_phone", row=2)
        self.create_attr_layout(self.add_services_input_frame, "client_email", row=3)
        self.create_attr_layout(self.add_services_input_frame, "client_adress", row=4)
        #self.create_attr_layout(self.add_services_input_frame,"services_number",row=5)

        self.push_services_button = customtkinter.CTkButton(self.tabview.tab("add new service"), text="push services",
                                                           command=self.push_service)
        self.push_services_button.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.check_service_frame = customtkinter.CTkFrame(self.tabview.tab("check service"))
        self.check_service_frame.grid(row=0,column=0)
        self.check_service_frame.grid_columnconfigure(0,weight=1)
        self.check_service_frame.grid_rowconfigure((0,1),weight=1)

        self.create_attr_layout(self.check_service_frame,"service_id")

        self.service_show_frame = customtkinter.CTkFrame(self.check_service_frame)
        self.service_show_frame.grid(row=2,column=0,columnspan=2)
        self.service_show_frame.columnconfigure((0,1),weight=1)

        self.service_show_update_button = customtkinter.CTkButton(self.check_service_frame,text="search",command=self.searchForService)
        self.service_show_update_button.grid(row=1,column=0,columnspan=2)
    def addlabel(self,root,message,row=0,name=""):
        frame = customtkinter.CTkFrame(root)
        frame.grid_columnconfigure((0,1),weight=1)
        frame.grid(row=row,padx=10,pady=10)
        customtkinter.CTkLabel(frame, text=message).grid(row=0)
        if name == "serviceDate":
            return
        btn = customtkinter.CTkButton(frame, text="edit",command=lambda : self.editView(name))

        btn.grid(row=0,column=1)
    def submitInput(self,window,name):
        self.set = True
        if name == "":
            return
        newVal = self.inputVar.get()
        if newVal == "":
            self.showMessage("your input is empty")
            return
        client = self.service_show_frame.client
        service = self.service_show_frame.service
        if name == "clientName":
            client.setFullName(newVal)
        if name == "clientPhone":
            client.phoneNumber = newVal
        if name == "servicePrice":
            service.price = newVal
        self.service_manager.saveJson()
        self.client_manager.saveJson()
        self.update_service_show()
        window.destroy()
    def getInput(self,message,name):
        self.inputVar = customtkinter.Variable(self)
        newWindow = customtkinter.CTkToplevel(self)
        newWindow.geometry("250x200+550+270")
        frame = customtkinter.CTkFrame(newWindow)
        frame.grid_columnconfigure((0, 1, 2), weight=1)
        frame.grid(row=0, column=0, rowspan=5, padx=0, pady=0)
        newWindow.grab_set()
        customtkinter.CTkLabel(frame, text=message).grid(row=0, column=1,padx=20,pady=20)
        customtkinter.CTkEntry(frame,width=200,textvariable=self.inputVar).grid(row=1,column=1,padx=20,pady=20)
        customtkinter.CTkButton(frame,text="ok",command=lambda: self.submitInput(newWindow,name)).grid(row=2,column=1)
    def target(self,k):
        pass
    def editView(self,name):
        self.getInput("enter the new " + name,name)


        
        print("sfdf")
    def addSubServiceFrame(self,frame,subService,row=0):
        newFrame = customtkinter.CTkFrame(frame)
        newFrame.rowconfigure((0,1,2),weight=1)
        newFrame.columnconfigure((0,1,2),weight=1)
        id = subService.id
        type = subService.type
        price = subService.price
        customtkinter.CTkLabel(newFrame,text=id,width=200).grid(row=0,column=0)
        customtkinter.CTkLabel(newFrame,text=type).grid(row=0,column=1)
        customtkinter.CTkLabel(newFrame,text=str(price),width=200).grid(row=0,column=2)
        newFrame.grid(row=row,column=0)
    def optionSelected(self,var,parent):
        option = str(var.get())
        idLabel = customtkinter.CTkLabel(parent, text='000')
        idLabel.grid(row=0, column=0)
        priceLabel = customtkinter.CTkLabel(parent, text='0')
        priceLabel.grid(row=0, column=2)
        print(option)
    def createSubServiceInputFrame(self,frame,row,service):
        newFrame = customtkinter.CTkFrame(frame)
        newFrame.rowconfigure((0),weight=1)
        newFrame.columnconfigure((0,1,2),weight=1)
        newFrame.grid(row=row,column=0)
        typeVar = customtkinter.Variable(newFrame)
        customtkinter.CTkOptionMenu(newFrame,width=200,values=self.subServiceType,variable=typeVar,command= lamda(self.optionSelected,{'var':typeVar,'parent':newFrame})).grid(row=0,column=1)
    def addSubServices(self,frameSource):
        newWindow = customtkinter.CTkToplevel(self)
        newWindow.geometry("660x660+330+0")
        frame = customtkinter.CTkFrame(newWindow)
        frame.grid(row=0, column=0, rowspan=5, padx=0, pady=0)
        newWindow.grab_set()
        newFrame = customtkinter.CTkFrame(frame)
        newFrame.columnconfigure((0,1,2),weight=1)
        newFrame.grid(row=0,column=0)
        customtkinter.CTkLabel(newFrame,text="id:",width=200).grid(row=0,column=0,pady=5)
        customtkinter.CTkLabel(newFrame,text="type:").grid(row=0,column=1)
        customtkinter.CTkLabel(newFrame,text="price:",width=200).grid(row=0,column=2)
        row=1
        for id, subService in frameSource.service.serviceDict.items():
            self.addSubServiceFrame(frame,subService,row)
            row +=1
        self.createSubServiceInputFrame(frame,row,frameSource.service)
        self.service_manager.saveJson()
    def update_service_show(self):
        frame = self.service_show_frame
        for child in frame.winfo_children():
            child.destroy()
        client = frame.client
        service = frame.service
        clientName = "client Name :   " + client.name + " " + client.lastName
        self.addlabel(frame, clientName, 0, "clientName")
        self.addlabel(frame, "service date :  " + str(service.date), 2, "serviceDate")
        self.addlabel(frame, "client phone :  " + str(client.phoneNumber), 1, "clientPhone")
        self.addlabel(frame, "price :  " + str(service.price), 3, "servicePrice")
        buttonFrame= customtkinter.CTkFrame(self.tabview.tab("check service"))
        buttonFrame.columnconfigure((0,1),weight=1)
        buttonFrame.grid(row=3,column=0)
        customtkinter.CTkButton(buttonFrame,text="add sub-services",command=lambda: self.addSubServices(frame)).grid(row=0,column=0)

    def show_service(self,service):
        frame = self.service_show_frame
        client = self.client_manager.findById(service.clientId)
        frame.client = client
        frame.service = service
        self.update_service_show()


    def searchForService(self):
        service_id = self.service_id_var.get()
        if service_id == "":
            self.showMessage("you must enter service id")
            return
        try:
            service_id = int(service_id)
        except:
            self.showMessage("id form wrong")
            return
        service = self.service_manager.findServiceById(service_id)
        if service == None:
            self.showMessage("service doesn't exist")
            return
        self.show_service(service)
    @staticmethod
    def trim(attrname):
        return attrname.replace("_"," ")
    def create_attr_layout(self,root,attrName,col=0,row=0,intoSelf=True):
        #self.__setattr__(attrName+"_frame",customtkinter.CTkFrame(root))
        #frame = self.__getattribute__(attrName+"_frame")
        #frame.grid_columnconfigure((0,1),weight=1)
        #frame.grid(row=row,column=col,padx=0,pady=0)
        frame = root
        label =customtkinter.CTkLabel(frame, text=self.trim(attrName))
        label.grid(row=row, column=0, padx=20, pady=(20, 10))
        #label = self.__getattribute__(attrName+"_label")
        var = customtkinter.Variable(self)
        #var = self.__getattribute__(attrName+"_var")
        entry = customtkinter.CTkEntry(frame,textvariable=var)
        entry.grid(row=row, column=1, padx=20, pady=(20, 10))
        #entry = self.__getattribute__(attrName+"_entry")
        if intoSelf:
            self.__setattr__(attrName + "_label", label)
            self.__setattr__(attrName + "_entry", entry)
            self.__setattr__(attrName + "_var", var)
        dict = {}
        dict[attrName + "_label"]=label
        dict[attrName + "_entry"] = entry
        dict[attrName + "_var"] = var
        return dict
    def push_service(self):
        imported= self.imported_var.get()
        if imported == 1:
            imported = True
        else:
            imported = False
        client_name = str(self.client_name_var.get())
        if client_name == "":
            self.showMessage("you must enter client name")
            return
        client_phone = str(self.client_phone_var.get())
        if client_phone == "":
            self.showMessage("you must enter client phone")
            return
        client_adress = str(self.client_adress_var.get())
        if client_adress == "":
            self.showMessage("you must enter client adress")
            return
        client_email = str(self.client_email_var.get())
        clientFullName = client_name.split(" ")
        client_name = clientFullName[0]
        client_lastName = ""
        for word in clientFullName[1:]:
            client_lastName += word+" "
        client_lastName = client_lastName[0:-1]
        client = self.client_manager.createClient(client_name,client_lastName,client_phone,client_adress,client_email)
        service = self.service_manager.createService(0,client.id)
        self.open_input_dialog_event(service)
        self.service_manager.saveJson()
        self.client_manager.saveJson()

    def showMessage(self,message):
        newWindow = customtkinter.CTkToplevel(self)
        newWindow.geometry("200x200+550+270")
        frame = customtkinter.CTkFrame(newWindow)
        frame.grid_columnconfigure((0, 1,2), weight=1)
        frame.grid(row=0, column=0, rowspan=5, padx=0, pady=0)
        newWindow.grab_set()
        customtkinter.CTkLabel(frame,text=message).grid(row=0,column=1)
    def open_input_dialog_event(self,service):
        #dialog = customtkinter.CTkInputDialog(text=("Type in a number:","khana"), title="CTkInputDialog")
        #service_price_entry = customtkinter.CTkEntry(dialog)
        #service_price_entry.grid(row=1,column=0)
        #print("CTkInputDialog:", dialog.get_input())
        newWindow = customtkinter.CTkToplevel(self)
        newWindow.geometry("200x200+550+270")
        #newWindow.grid_columnconfigure((0,1,2),weight=1)
        #newWindow.grid_rowconfigure((0,1,2),weight=1)
        frame = customtkinter.CTkFrame(newWindow)
        frame.grid_columnconfigure((0, 1), weight=1)
        frame.grid(row=0,column=0,rowspan=5,padx=50,pady=50)
        newWindow.grab_set()
        customtkinter.CTkLabel(frame,text = "the service id is :"+str(service.id),justify="center").grid(row=0,column = 1)



    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
    def mainloop(self, *args, **kwargs):
        super().mainloop(*args,**kwargs)
        print(self.client_name_var.get())
        print(self.imported_var.get())

if __name__ == "__main__":
    app = App()
    app.mainloop()