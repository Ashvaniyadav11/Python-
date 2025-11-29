#OOPS Pillar   4 typees


#Encapsulation
#Wrapping data & functions into Single Unit --- Data hiding

#data hinding
#1.public _--> acces inside and outside the class
#2.proctected ---> acces class + subclass
#3.private --> access inside the class 

# data + methods = class 


class BankAccount:
    def __init__(self,name,balance):
        self.name = name #public
        self.__balance = balance #protected  
    def get_balance(self):
        return self.__balance

acc1 = BankAccount("Randwa Khan",100_0000)

print(acc1.name,acc1.get_balance())




# BY convention hota 