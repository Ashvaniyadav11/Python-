class Product_store:
    count = 0
    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product_store.count += 1
    @classmethod
    def get_count(cls):
        print(f"Total number count is : {cls.count}")
    
    def get_info(self):
        print(f"Price of  {self.name} is Rs {self.price}")
    @staticmethod
    def cal_dis(price, discount):
        New_price = price - (discount * price / 100)
        print(f" Discount price is {New_price}")
      
    
   

l1 = Product_store("Laptop",20_000)
l2 = Product_store("phone",10_000)
l3 = Product_store("Pen",1000)

l1.get_info()

l1.cal_dis(l1.price,18)

Product_store.get_count()