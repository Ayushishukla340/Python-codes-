# class Employee:
#   company = "HCL"
#   name = "Ayushi"

#   def show(self):
#     print(f"The of name of employee is {self.name} and the company is {self.company}") 

# class Coder: 
#   language = "Python"  
#   def printLanguages(self):
#     print(f"Out of all the languages here is your language : {self.language}")

# class Programmer(Employee, Coder):
#   comapny = "HCL TECH"
#   def showLanguage(self):
#     print(f"The name is {self.name} and he is good with {self.language} language")

# a = Employee()    
# b = Programmer()

# print(a.company, b.company)

# b.show()
# b.printLanguages()
# b.showLanguage()







# class Employee:
#   a = 12

# class Programmer(Employee):
#   b = 24

# class Manager(Programmer):
#   c = 36

# o = Employee()
# print(o.a)  # prints the a attribute

# o = Programmer()
# print(o.a , o.b)

# o = Manager()
# print(o.a , o.b, o.c)









# class Employee:
#     def __init__(self):
#         print("Constructor of employee")
#         self.a = 12

# class Programmer(Employee):
#     def __init__(self):
#         super().__init__()   # Employee constructor call
#         print("Constructor of Programmer")
#         self.b = 24

# class Manager(Programmer):
#     def __init__(self):
#         super().__init__()   # Programmer constructor call
#         print("Constructor of Manager")
#         self.c = 36

# o = Employee()
# print(o.a)

# o = Programmer()
# print(o.a, o.b)

# o = Manager()
# print(o.a, o.b, o.c)












