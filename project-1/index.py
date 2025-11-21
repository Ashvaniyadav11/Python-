

def binaryy(n,op):
    if(op == "bin"):
        s = bin(n)
        return s
    elif(op == "oct"):
        s = oct(n)
        return s
    elif(op == "hex"):
        s = hex(n)
        return s
    elif(op == "dec"):
        print(n)

    else:
        print("You are chutiya ")
        
n = int(input("Enter the value of n \n"),0)
d = (input("where you want to convert it \n"))

print(binaryy(n,d))