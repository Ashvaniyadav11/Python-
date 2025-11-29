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