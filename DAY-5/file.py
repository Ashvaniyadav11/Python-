# file I/O means method file input and output

#open and operation,close and delete

#open     file name or path
##f = open("data.txt" ,"r")
                    #mode =. read mode r and write mode w

#Example
'''
f = open("new.txt", "r")  # open returns a file object
data = f.read() 
data = f.readline() #data ko read krta hai line by line  ek line read karega


f = open("new.txt", "w") #yha pe w krna hoga 
f.write("the complete data \n i love you girl")
print(data)

f.close() #Always close your always if you 



#modes in file
#with keyword use krne se hame file close krna nhi padhta hai

with open("data.txt" , "r") as f:
    data = f.read()
    print(data) 


#Delete files 
#os module use tu delete 

import os 

os.remove("sample.txt")
'''
"""
r     #reading(defult)
w     #writing trunctes(complete file ko saaf kr deta hai) file first
x     #creates new & open and write (jb hame new file bana hai )
a     #writing ,append at end (pura data eraze nhi krta hai jha se end hota uha se data add kr ta hai )
b     #Binary mode 
t     #text mode (default)
+     # open disk file for (r&w ) dono mode ka use krsakte hai (r+)


f = open("hello.txt","a+")
f.write("\nHello Basanti")

"""
#world search 
data = True
line = 1
word = "Python"
with open("hello.txt","r") as f:
    while data:
        data = f.readline()

        if(word in data):
            print(f"we found at line no  {line}")
            break
       
        line += 1
       


#Exception Handling
#try ,exept ,else ,finally

#try 
try:
    x = int(input("enter x\n"))
    ans = 10/x
except ZeroDivisionError:
    print("divide by zero not allowed\n")
except ValueError:
    print("This is not allowed")

else:
    print(f"Answer is {ans}")

finally:
    print("End of Pyhton program")


#list comprehensions
#[ouput for item in iterable if conditon ]

square = []

for i in range(7):
    square.append(i*i)
print(square)

sq = [i*i for i in range(7) if i%2 !=0]
print(sq)

#[-2,-3,-4,3,45,65,6,-8,3,-1]

num = [-2,-3,-4,3,45,65,6,-8,3,-1]
num = [ 0 if val < 0 else val for val in num]

print(num)


words = ["helo","python","apna college"]
words = [val.upper() for val in words]

print(words)


#Json Module 
#import json
# json format has key:value 
#json.loads() s stand for string

'''

import json

json_str = '{"name":"Ashvani","isStudent": true,}'

py_obj = json.loads(json_str)

print(type(py_obj),py_obj)'''

import json
py_obj = {
    "name":"Ashvani",
    "isteacher":True
}
json_str = json.dumps(py_obj)

print(type(json_str),json_str)


import json

with open("data.json","r") as f:
    py_obj1 = json.load(f)
    print(py_obj1)
    print(type(py_obj1))

import json 

data = {
    "name":"Uttam",
    "age":27,
    "isteacher":False
}

with open("data.json","w") as f:
    json.dump(data,f,indent=4,sort_keys=True)