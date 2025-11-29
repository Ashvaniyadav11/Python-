#methods are 3 type
#1.instances 
#2. Class
#3.Static method




#1.instances          #2.class                   Static(logically claases ke sath typed hote hai )
# 1st parameter     # 1st parameter is       #no compulsory parameter
#self likhna          "cls" refecing class
#  compulsory

#2 they can acces    #2. acces only class   #no instances
#the class as well                          #class
#as instance attribtes # decorator          #@staticmethod
                        #"classmethod"


class Laptop:
    storage_type = "SSD"
    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage

    def get_info(self):  #instances method
        print(f"Laptop has {self.RAM} & {self.storage} {self.storage_type}")
    @classmethod #means  basically it a function take another function behaviour change kr wapas return kr deta hai
    def get_storage_type(cls):
        print(f"storage type = {cls.storage_type}")

    @staticmethod
    def cal_distount(price,discount):
        final_price = price - (discount * price / 100)
        print(f"Discount price = {final_price}")

l1 = Laptop("16gb" , "512gb")
l2 = Laptop("8gb" , "252gb")

l1.get_info()
l2.get_info()
Laptop.get_storage_type() 
l1.get_storage_type() #object has higher prority to acces the class



l1.cal_distount(40_000,10)  #
