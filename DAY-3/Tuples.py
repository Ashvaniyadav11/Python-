#tuples are immutable sequence of value created with ()

tup = (1 ,2,34,54 ,"abc",3.14)

print(tup)
#tup = (1) #expression we cannot create this 
# we can make t with one comma(,)

print(tup[2:5])

tuuup = (1,2,3,2,2,2,4,5,6)

sum = 0
for val in tuuup:
    sum += val
print(f"Sum of the tuples is {sum}")

#Method of tuples
#t.index(val) #returns 1St occurance idx
#t.count(val) #counts total occurance

#---> its go left to right
print(tuuup.index(2))
print(tuuup.count(2))


