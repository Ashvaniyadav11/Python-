#Loops are basically use print  for repeatation

#while if condition is true it repeat himself when condition is true 

''' 
count = 1
while count < 6:
    print("HW")
    count += 1
print("after loop , count + ", count) 


#print number 1 to 5
count = 1
while count < 6:
    print(count)
    count += 1

#reserse the number 
count = 5
while count >= 1:
    print(count)
    count -= 1

#print multiplication of table of any number n

n = int(input("Enter the number \n"))

i = 1
while i < 11 :
    print(n * i)
    i += 1

    
#break and continue 
# break is use to stop the loop
# continue is use to skip the that a line

i = 1
while (i <= 10):
    if(i % 6 == 0):
        break
   # print(i)
    i += 1

i = 1
while (i <= 10):
    if (i % 3 == 0):
        i += 1
        continue
   # print(i)
    i += 1

#print odd number from 1 to 10
# 
i = 0
while (i < 10):
    i += 1
    if (i % 2 == 0):
        
        continue
    print(i)
    
#for loop is used for sequential traversal

#for variable in kuch string ,tuple etc

string = "hello"
# if 'o' in string:
#     print("o is exist ")
#in is called membership operator  jo basically kisi seqence ko track krta hai
# in basicaally to check presence
for var in string:
    print(var)


#for i in range(5):
    #print(i)
word = "artificial intelligence"

ans = 0
for i in word:
    if i == 'i':
        ans += 1
print(ans)    



#print vowel count of a given string

let = "ashutosh kumar pandey i trusted apnaCollege & enrolled in alpha in my 2nd year for placement preparation. it gave me a good path to follow along with a streamlined syllabus. the batch supported me a lot."
count = 0
for i in let:
    if( i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' ):
        count += 1
        
print(count)

#range  function is used to generate sequence
#range(n) means 0 to n-1

#range(start, stop ,step) // stop value must be needed

for i in range(1,10,2):
    print(i) # 1 3 5 7 9


n = int(input("Enter the number\n "))
sum = 0
for i in range(1,n+1):
    sum += i
print("sum of ",n," is ",sum)
'''