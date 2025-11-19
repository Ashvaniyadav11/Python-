'''
#Problem --1
#Write a program that asks the user for their name and age, then prints a
#sentence like:

name = str(input("Enter Your Name :\n"))
age = int(input("Enter your age :\n"))

print("Hello ",name," you are",age ,"years old")


#Hello  Ashvani Yadav  you are 20 years old


#Problem --2
#Take two numbers as input from the user and print their sum, difference,
#product, and quotient.

a = int(input("Enter the number a  :\n"))
b = int(input("Enter the number b  :\n"))

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a**b)


#Problem --3
#Ask the user to enter two integers and one float. Convert them all to floats
#and print their average

a = int(input("Enter the number a  :\n"))
b = int(input("Enter the number b  :\n"))
c = float(input("Enter the number c  :\n"))

sum = a + b + c
avg = sum / 3

print("Your average is : " , avg)


#Problem --4
. The user enters a string containing a number (e.g."45" ). Convert it to:
• an integer
• a float
• a string again
Print all three values with their types


a = "45"
x = int(a)
print("Integer form : ", x, "\ntype of check" ,type(x))
#Integer form :  45 
#type of check <class 'int'>

z = float(a)
print("In float form : ", z, "\ntype of check" ,type(z))
#In float form :  45.0
#type of check <class 'float'>

y = str(a)
print("In String form : ", y, "\ntype of check" ,type(y))
#In String form :  45
#type of check <class 'str'>



#Problem --6
#Write a program to swap values of two numbers entered by the user
a = int(input("Enter the number a  :\n"))
b = int(input("Enter the number b  :\n"))
temp = a
a = b
b = temp
print("a is : ",a,"\nb is : ",b)



#Problem --6
. Ask the user for a temperature in Celsius (string input). Convert it to ,
then calculate and print temperature in Fahrenheit.
Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) +
32


TemperatureINCelcius = str(input("Enter temperature in celcius\n"))

T_C = float(TemperatureINCelcius)

FahrenheitTemp = (T_C * (9/5)) + 32

print("Temperature in Farenheit is : ", FahrenheitTemp)


#Problem --6
Take the radius (r) as user input and print the area.
Use the formula: Area = π * r
 (value of π = 3.14)



radius = float(input("Enter the radius  :\n"))
pi = 3.14
areaofcicle = pi * radius ** 2

print("Circle are is : ", areaofcicle)



#Problem --6
Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and
compute simple interest:
SI = (P ∗ R ∗ T)/100



p = float(input("Enter the principal :\n"))
r = float(input("Enter the rate  :\n"))
t = float(input("Enter the Time  :\n"))

si = (p * r * t)/100

print("Simple interest is : " , si)



#Problem --6
 Take a decimal number as input (like ) and output its:
• integer part -
• fractional part -
45
.78
'''

ff = float(input("Enter the float type value :\n"))

new_ff = int(ff)

fff = ff - new_ff

print("Interger value is : ", new_ff,"\n Fractional part is :",fff)

