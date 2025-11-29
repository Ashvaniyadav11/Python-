
#String is the collection of characters

#we can create string single kot and double kot
#in string strore seqeance of character

##Creating a string
word = "pyhton"
word2 = "Developer"

##empty string
s = ""
print(s)
print(type(s)) #<class 'str'>

#STRING FUNCTIONS
print(len(word))

# concatinate
print(word + " " + word2)

#STRING REPETITION
print("Hi" * 3)  # HiHiHi


# we can also do indexing(0 to n-1) in string

for ch in word:
    print(ch)

# string is immutable
# hum kisi bhi particular string ko change nhi kr sakte hai

#slice in strings (sub string)
str = "python"
     #   -6,     -2,-1 reverse indexing
#str[st index:end index]
print(str[2:4]) #th
print(str[:])

#Upper / Lower

d = "hellO"
print(d.lower())  #hello
print(d.upper())  #HELLO

print(d.strip())  # hellO       #remove both side spaces
print(d.lstrip())  # hellO       #left only
print(d.rstrip())  #   hellO  #right only


print(d.startswith("he"))  #True
print(d.endswith("on"))    #False

print(d.split())     #['hellO']

#CHECKING STRING CONTENT
print(d.isalpha() ) #True      # only letters?
print(d.isdigit())  # false    # only digits?
print(d.isalnum())   #True     # letters + numbers?
print(d.isspace())    #False         # only spaces?
d.isupper()
d.islower()












#String formatting --> jb hum dynamically  string ko create krte hai
# Dynamically means different varibale and different value ko use krte hai

#1 way using format() function
#placeholder use {} 
a = 5
b = 10 
sum = a + b
# normal formatting
print("sum is {}".format(sum))
print("summ of {} and {} is {} ".format(a,b,sum))

#index based formating
print("summ of {1} and {2} is {0} ".format(a,b,sum))
#value based formatting 
print("summ of {a} and {b}  ".format(a =15,b = 11))

#2 f-string
#Literal string interporation --> string ke ander kahi bhi kr sakte hai

a = 23 
b = 45

print(f"sum of {a} & {b} is {a + b}")
