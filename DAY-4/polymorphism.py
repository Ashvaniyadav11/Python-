#polyMorphism == many forms

#operator overloading --> add and concatination


#1. Function overiding(Inheritance)
#2. Duck Typing ---walk like duck & quaks like  duck






class Employee:
    def get_designation(self):
         print("This is designation")
    
    
    

class Teacher(Employee):
    def get_designation(self):
          print("This is designation")

  



t1 = Teacher()
t1.get_designation()



class Teacher():
    def get_designation(self):
          print("This is designation = Teacher")


class Acountant():
    def get_designation(self):
          print("This is designation = Acountant")


t1 = Teacher()
t1.get_designation()

acc1 = Acountant()
acc1.get_designation()