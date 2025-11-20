#Conditional Statement
#if,elif,else

#if 
'''
if condition :
  #code

#Example
age = int(input("Enter your age Now\n"))

if age >= 18:
  print("You can vote ")
  print("You can Sex ")
  elif 
else:
  print("You Not vote and Sex")

  #traffic light
color = str(input("Enter color name\n"))

if color == "red":
    print("please Stop")
elif color == "yellow" :
    print("Ready for Going")
elif color == "green":
    print("You can GO")
else:
    print("Wrong color of trafic light")

 
#problem 
#checking age 
age = int(input("Enter your age \n"))

if age < 13:
    print("Child")
elif age >= 13 and age < 18:
    print("You cannot Sex Only make setting")
else:
    print("You can do both vote and sex ")

#Giving permission for Logging
username = str(input("Enter username\n"))
password = str(input("Enter password\n"))

if (username == "admin" and password == "pass"):
    print("You login is succesful")
elif(username != "admin"):
    print("Wrong username")
else:
    print("Wrong password")

#Checking multiple of 5

n = int(input("Enter the number\n"))

if (n%5 ==0):
    print(n ,"multiple of 5")
else:
    print(n,"not multiple of five")

    

#Number  is odd or even

n = int(input("Enter the number\n"))

if(n%2 ==0):
    print(n,"Even number")
else:
    print(n,"Odd number")


#NESTING ek conditional statement another conditonal statement

username = str(input("Enter username\n"))
password = str(input("Enter password\n"))

if (username == "admin" and password == "pass"):
    print("You login is succesful")
else:
    if username != "admin":
        print("Wrong username")
    else:
        print("Pasword is not correct")

        
#Match Case -- basically an alternative for if elif else

color = str(input("Enter color name\n"))

match color:
    case "green":
        print("GO")
    case "yellow":
        print("Look")
    case "red":
        print("Stop")
    case _: #Deafault
        print("Wrong color entered")
'''


