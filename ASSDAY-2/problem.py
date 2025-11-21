'''
. Write a program that takes as input salary. Using conditional statements, 
calculate the final tax rate based on these rules: 
• If salary < 30,000 → 5% 
• If salary is 30,000–70,000 → 15% 
• If salary > 70,000 → 25%

salary = float(input("Enter your Salary\n"))

if(salary <30000):
    tax = salary * 5 / 100
    new_salary = salary - tax
    print("New salary is : ",new_salary,"\nTax is ",tax)
elif(salary >= 30000 or salary <70000):
    tax = salary * 15 / 100
    new_salary = salary - tax
    print("New salary is : ",new_salary,"\nTax is ",tax)
else:
    tax = salary * 25 / 100
    new_salary = salary - tax
    print("New salary is : ",new_salary,"\nTax is ",tax)


# Write a function that takes two integers and and prints all even 
#numbers between them (inclusive). 

def sum(a,b):
    for var in range(a,b):
        if(var%2 == 0):
            print(var)

m = int(input("Eneter starting number :\n"))
n = int(input("Eneter starting number :\n"))

sum(m,n)

# Write a function that prints the digits of a number, . 
#For eg: , there are 3 digits in it 3, 1 and 2 & we need to print them.

def splitter(n):
    while (n>0):
        s = n%10
        print(s)
        n = n//10
    
    
      
splitter(312)


#Write a function to return the count the number of digits in a number n, 
def digit_counter(n):
    count = 0
    while(n>0):
        count += 1
        n = n//10
    return count

n = int(input("Enter the number of Digit\n"))
print(digit_counter(n))


# Write a function to return the sum of digits of a number

def summ(n):
    sum = 0
    for i in range(1,n+1):
        sum += i

    return sum
n = int(input("Enter the number of Digit\n"))
print("Sum of total :",summ(n))


# Write a program to print all numbers from 1 to 100 that are divisible by both 3 
#and 5
def rangeinbt(a,b):
    for i in range(a,b):
        if(i%3==0 and i%5==0):
            print(i)
        
rangeinbt(1,100)


while(True):
    n = input("Enter the quit for stop\n")
    if(n=="quit"):
        break;
    new = float(n)  
    if(new >= 0):
        print(new ,"is postive number")
    else:
        print(new ,"is negative number")
 #Building calculaotr
def calculator(a, b, op):
    match op:
        case '+': return a + b
        case '-': return a - b
        case '*': return a * b
        case '/': return a / b
        case _ :  return "Invalid operator"



a= float(input("Enter the Digit\n"))
b= float(input("Enter the Digit\n"))
c= str(input("Enter the Digit\n"))


print(calculator(a,b,c))

#Write a function isprime that returns true value

def is_prime(n):
    if(n<=1):
        return False
    for i in range(2,n):
        if n%i == 0:
            return False
        
    return True    
n = int(input("Enter the n\n"))
print(is_prime(n))


'''
secret_num = 52

while(True):
    guess = int(input("Guess the number\n"))
    if(guess > secret_num):
        print("Too High")
    elif(guess < secret_num):
        print("Too Low")
    else:
        print("Corrrect number guessed")
        break;