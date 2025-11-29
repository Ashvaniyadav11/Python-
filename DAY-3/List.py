
#Lists
#Lists use square brackets []
# mutable  sequence of values
# follow indexing in list
# list ke ander hum hr tarah ki value store kra sakte hai
marks = [99,34,65,87,100]

print(marks)
print(len(marks))
print(marks[-1])

#Properties of Lists

# Ordered
#  Mutable (you can change items)
# Can store multiple data types
# Allows duplicates
# Indexing & slicing supported

#mixed list 
lst = [10, "Ashvani", 3.14, True]


#Empty list
lst = []



#updatedation
marks[2] = 100

print(type(marks))
#when we slicing it known as sublist
print(marks[0:3])


# Method or functions 
#l.append(val) # add one element at the end
#l.insert(idx,val)#insert element at iindex
#l.sort() # arrange in increasing order
#l.reverse() #reverse order
l = [1,2,3,4,6]
l.append(23)

print(l)

l.insert(2,10)
print(l)

l.sort()
print(l)

l.sort(reverse=True) # decreasing
print(l)


#using loop in list most use for loops

nums = [11,2,3,10,4,5,6,7]

x = 10
idx = 0
for val in nums:
    if(val == x):
        print("idex is ",idx)
        break
    idx += 1

