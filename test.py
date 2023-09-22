from datetime import datetime
class ob:
    def __init__(self,name):
        self.name = name
        self.__setattr__("name",name)
    def setAge(self,age):
        self.__setattr__("age",age)
    def __str__(self):
        txt = ""
        for att, val in self.__dict__.items():
            txt += str(att) + str(val)
        return txt
obb = ob("zakaria")
obb.setAge(100)
lst = [1,1,1]
lst1 = lst
lst1 = 0,0,0
print(lst)
print(**{'s':"dsad","dsa":"da"})