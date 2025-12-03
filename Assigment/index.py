''' Create a 
BankAccount 
class with attributes account_number, owner_name, 
and balance. 
Add methods to deposit, withdraw, and check balance.
'''

class BankAccount:
    def __init__(self,owner_name,account_number ,balance = 0):
        self.owner_name = owner_name
        self.account_number = account_number
        self.balance = balance


    def deposit(self,amount):
        if amount > 0 :
            self.balance += amount
            print(f"Rs{amount} Deposited succesfully")
        else:
            print("Amount should be positive")
    
    def withdraw(self,amount):
        if amount <= 0:
            print("withdraw ammount should be positive")
        elif amount > self.balance:
            print("Insufficient Balance")
        else :
            self.balance -= amount
            print(f"Rs {amount} deducted succesfully")
    
    def check_balance(self):
        print(f"Your avaible balance is {self.balance}")
        

acc1 = BankAccount("Ashvani Yadav",239901128474,23)

acc1.deposit(35_0000)
acc1.withdraw(34_000)
acc1.check_balance()



"""
2. Create a BOOK class with the following attributes: 
• title 
• author 
• list of reviews 
And add methods to: 
• add a new review 
• count reviews 
• display all reviews
"""
class Book:
    
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.list_of_reviews = []   # always a list

    def add_reviews(self, review):
        if 1 <= review <= 5:
            self.list_of_reviews.append(review)
            print(f"Your review got added: {self.list_of_reviews}")
        else:
            print("Enter review between 1 to 5")
    def Display(self):
        if self.list_of_reviews == 0:
            print("No reviews is avaible")
        else:
            for var in self.list_of_reviews:
                print(f"-{var} ")
        

    

book1 = Book("Madhur", "French")
book1.add_reviews(4)
book1.add_reviews(5)
book1.add_reviews(10)   # will show error
book1.Display()


'''
Create a class 
Student 
with private attributes _name, _roll_no, and _marks. 
Provide getter and setter methods with validation (e.g., marks cannot be 
negative, roll number has to be between 1 & 100 & name cannot be empty). 
'''

class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no) #set use krne se name blank nhi ho sakta hai
        self.set_marks(marks)

    # ----- NAME -----
    def get_name(self):
        return self.__name

    def set_name(self, name):
        if name.strip() == "":
            raise ValueError("Name cannot be empty.")
        self.__name = name

    # ----- ROLL NUMBER -----
    def get_roll_no(self):
        return self.__roll_no

    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self.__roll_no = roll_no
        else:
            raise ValueError("Roll number must be between 1 and 100.")

    # ----- MARKS -----
    def get_marks(self):
        return self.__marks

    def set_marks(self, new_marks):
        if new_marks < 0:
            raise ValueError("Marks cannot be negative.")
        self.__marks = new_marks

stu1 = Student("Ashvani Yadav",14,90)
print(stu1.get_marks())
stu1.set_marks(98)
print(stu1.get_marks())

'''
Concept: Function Overriding 
Rectangle 
Q4. Create a class Shape with a method area(). 
Create subclasses Circle , , and that override the area() 
method. 
'''

class Shape:
    def area(self):
        return "Area is not defined for Shape"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# ------- Testing ---------
c = Circle(5)
r = Rectangle(4, 6)
t = Triangle(10, 5)

print("Circle area:", c.area())
print("Rectangle area:", r.area())
print("Triangle area:", t.area())

"""
 Inheritance 
Q5. Create a base class Vehicle with attributes like brand and model. 
Create two subclasses Car and Bike that add extra attributes - seats (in Car) & 
engine_cc (in Bike).
"""

class Vehicles:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Car(Vehicles):
    def __init__(self, brand, model,seatts,engine_type):
        super().__init__(brand, model)
        self.seatts = seatts
        self.engine_type = engine_type
    
    def get_seaters(self):
        return self.seatts

class Bike(Vehicles):
    def __init__(self, brand, model,engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc
    def get_ccdetail(self):
        return self.engine_cc
    


bike1 = Bike("Tesla",2022,"250cc")

print(bike1.get_ccdetail())

car1 = Car("tata",2025,7,"Diesel")

print(car1.get_seaters())

'''
oncept: Abstraction 
Q6. Create an abstract class 
Employee 
calculate_salary(). 
Create subclasses , 
Intern 
with an abstract method 
FullTimeEmployee 
implement the method differently. 

'''
from abc import ABC,abstractmethod
class Employee:
    @abstractmethod
    
