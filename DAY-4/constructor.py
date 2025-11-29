#constructor oo function jo hota jo kisi object ko construct krta hai
#_init_method = call every time to create object
#this method is use ko inilise our object

#class Student:
   # def __init__(self): #self = it is storing the current instance of class means that is storing refeerce of current object 
                #self is complesury it use to write
     #   print("THat constructor was called")
#Example
class Student:
    def __init__(self,name,cgpa):
        self.name = name
        self.cgpa = cgpa
    def get_cgpa(self):
        return self.cgpa
stud1 = Student("rishi",9.1) # jitne hum object bnayege utni bar #constructor call hoga
stud2 = Student("prajjwal",9.2) #constructor object ke liye ek baar call              #hota hai jb hum oject ko bnate hai
stud3 = Student("Ashvani Yadav" ,9.4)
stud4 = Student("Nitin kumar sing",8.3)
print(stud1.name)
print(stud1.cgpa)
print(stud2.name)
print(stud2.cgpa)
print(stud3.name)
print(stud3.cgpa)
print(stud4.name)
print(stud4.cgpa)


print(stud1.get_cgpa())





#type of constructor
#1.default  sirf ek hi hota hai --- self
#2parametrised self ke alava --- a,b,c,d
#hr class me one construcor and one init method
