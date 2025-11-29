# class attributes belong to class hr object ke liye common 
#instance belong to object ye different

class Student:
    college_name = "ABC COLLEGE" #Class
    PI = 3.1
    def __init__(self,name,cgpa): #Instances has higher property
        self.name = name
        self.cgpa = cgpa
        self.PI = 3.14

stu1 = Student("Ashvani Yadav",9.1)

print(stu1.name,stu1.cgpa)
print(stu1.college_name)
print(stu1.PI)  #jb do variable same name ke hote hai to jyada prority instance ki hoti hai
print(Student.PI)