# class Employee:
#   language = "JAVA"    #this is a class attribute
#   salary = 1200000
#   company = "HCL" 

# def __init__(self):    #dunder method which is automatically called 
#   print("I am creating an object")

# def getInfo(self):
#   print(f"The lang is {self.language}. The salary is {self.salary}")

#   @staticmethod
#   def greet():
#     print("Good morning, sir")

# harry = Employee()    
# harry.name = "Harry"
# print(harry.name,harry.salary,harry.company)








# class Employee:
#     language = "JAVA"    # class attribute
#     salary = 1200000
#     company = "HCL" 

#     def __init__(self, name, salary, language, company):  #dunder method which is automatically called 
#         self.name = name 
#         self.salary = salary
#         self.language = language
#         self.company = company
#         print("I am creating an object")

#     def getInfo(self):
#         print(f"The lang is {self.language}. The salary is {self.salary}")

#     @staticmethod
#     def greet():
#         print("Good morning, sir")


# harry = Employee("Harry", 20000000, "Python", "Infosys")    
# print(harry.name, harry.salary, harry.language, harry.company)

# Employee.greet()
# harry.getInfo()








# class Programmer:
#   company = "Microsoft"
#   def __init__(self, name, salary, pincode) :

#     self.name = name 
#     self.salary = salary
#     self.pincode = pincode

# p = Programmer("Ayushi Shukla", 1200000, 208021)
# print(p.name, p.salary, p.pincode )  

# d = Programmer("Divya Yadav", 10000, 208011) 
# print(d.name, d.salary, d.pincode )  

# a = Programmer("Aarti Shukla", 230000, 208021) 
# print(a.name, a.salary, a.pincode )  

# r = Programmer("Ranjali Mishra", 1200000, 206012) 

# print(r.name, r.salary, r.pincode )  






# class calculator:
#   def __init__(self,n):
#     self.n = n

#   def square(self):
#     print(f"The square is {self.n * self.n}")

#   def cube(self):
#     print(f"the cube is {self.n * self.n * self.n}")

#   def squareroot(self):
#     print(f"the square root is {self.n**1/2}")  

# a = calculator(4)
# a.square()
# a.cube()  
# a.squareroot()  






# class Demo:
#   a = 4

# o = Demo()  
# print(o.a)   #prints the class attribute because instance attribute is not present

# o.a = 0  # instance attribute is set 
# print(o.a)   #prints the instance attribute because instance attribute is present
# print(Demo.a)







# from random import randint

# class Train:

#   def __init__(self, trainNo):
#       self.trainNo = trainNo

#   def book(self, fro, to):
#     print(f"Ticket is  booked in train no: {self.trainNo} from {fro} to {to}")

#   def getStatus(self,):
#         print(f"train no: {self.trainNo} is running on time")

#   def getFare(self, fro, to):
#        print(f"Ticket fare  in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")

# t = Train(12349)
# t.book("Balrampur","Mumbai")
# t.getStatus()
# t.getFare("Balrampur", "Mumbai")




















