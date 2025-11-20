# Function
'''
block of statement that perform specific task
definition and call(invoke)

syntax: def fxn_name():



def hello():
    print("Hello developer")
hello()
# parameter => logic => return

#sun of two numbers
def sum(a,b):
    return a + b
c = sum(23,34)
print(c)

#average of three numbers
def avg(a,b,c):
    return (a+b+c)/3
print(avg(10,10,40))


#type of function 
#built-in function and user defined function

#Lambda Function

#lambda a,b,c:___________Expression
#uses in high order function
sum = lambda a,b,c: a+b+c
print(sum(23,45,65))



# FActorial of any number
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
n = int(input("Enter the number\n"))
print(factorial(n))

'''
    


