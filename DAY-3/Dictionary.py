#Dictionary : ke ander key value pairs hote hai created {}
#key:value pairs
#mutable 
#unordered
dict = {
    "name":"ashvani Yadav",
   " cgpa":9.2,
   "subjects":["math ,science"],


}

print(dict)
print(type(dict))
print(dict["name"]) # dict ke ander value accces kr sakte hai

dict[" cgpa"] = 10.0
print(dict)


#Methods in dictionary
#d.keys()  #returns
#d.values() # returns all values
#d.items() #returns (Key , val) pairs
#d.get(val) #nreturns val acc. to key
#d.update(new_item) #adds new items to dictionary

print(dict.keys())

