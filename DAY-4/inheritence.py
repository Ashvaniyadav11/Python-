#inheritence
#reusing attr and method from a parent (Base) class


class Employee:
    start_time = "10 am" 
    end_time  = "4pm"
    def change_time(self,new_endtime):
        self.end_time = new_endtime



class Teacher(Employee):   #inherhentane
    def __init__(self,subject):
        self.subject = subject   #subclass


class Admin(Employee):
    def __init__(self,role):
        self.role = role


staff1 = Admin("Manager")



t1 = Teacher("math")
t1.change_time("6pm")

print(t1.subject,t1.start_time,t1.end_time)


#Types of Inheritance
#1. Single level inheritance ----one parent to one child
#2. Multi level inheritance -- one parent to one child to one subchild
#3.multiple Inheritance 

#2. Multi level inheritance Example

class Employeee:
    start_time = "10 am" 
    end_time  = "4pm"

class Adminn(Employeee):
    def __init__(self,role):
        self.role = role

class Accountant(Adminn):
    def __init__(self,salary, role):
        super().__init__(role)  #super key word is use to acces the parent property
        self.salary = salary

acc1 = Accountant(25_000,"CA")

print(acc1.role,acc1.salary,acc1.start_time,acc1.end_time)



#3.multiple Inheritance

class Teacher:
    def __init__(self,salary):
        self.salary = salary

class Student:
    def __init__(self,gpa):
        self.gpa = gpa

class TA(Teacher ,Student):
    def __init__(self, salary ,gpa,name):
        super().__init__(salary)
        self.name = name
        Student.__init__(self,gpa)

ta = TA(15_000,9.3,"Ashvani Yadav")

print(ta.name,ta.salary,ta.gpa)