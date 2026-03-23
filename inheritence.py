# (INHERITENCE ................................)



# class Animal:
#   def speak(self):
#     print("Animals make sound")

# class Dog(Animal):
#   def bark(self):
#     print("dog barks ")
# d = Dog()    
# d.speak()
# d.bark()




# class Animal:
#   def sound(self):
#     print("some generic sound ")
# class Cat(Animal):
#   def sound(self):
#     print("Meow !!!!")
# a =Animal()       
# c = Cat()
# a.sound()
# c.sound()




# (((####ENCAPSULATIONN.......))).......................



# class BankAccount:
#   def __init__(self,owner,balance):
#     self.owner = owner
#     self.__balance = balance    #balance attribute
#   def deposit(self,amount):
#     self.__balance += amount

#   def get_balance(self):
#     return self.__balance
# acc = BankAccount("Alice ", 10000)  
# acc.deposit(5000)
# print(acc.get_balance())




# class Student:
#   def __init__(self,name,roll_no,marks):
#     self.name = name
#     self.roll_no = roll_no
#     self.marks = marks
#   def display_details(self):
#     print("Name",self.name)
#     print("Roll_no",self.roll_no)
#     print("Marks",self.marks)

# s1 = Student("Ayushi - ", 57 , 99) 
# s2 = Student("Suhani - ", 43 , 56)  
# s3 = Student("Yashi - ", 67 , 20)  
# s4 = Student("Kumkum - ", 27 , 45)  

# s1.display_details()
# s2.display_details()
# s3.display_details()
# s4.display_details()



# import math

# class Circle:
#   def __init__(self,radius):
#     self.radius = radius
#   def area(self):
#     return math.pi * self.radius * self.radius
#   def circumference(self):
#     return 2 * math.pi * self.radius
# c1 = Circle(4)  

# print("Area of circle : ", c1.area())
# print("Circumference of circle : " , c1.circumference())




# class Person:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age

# class Employee(Person):
#   def __init__(self,name,age,salary):
#     super().__init__(name,age)
#     self.salary = salary
#   def display(self):
#    print("Name - ", self.name)    
#    print("Age - ", self.age)    
#    print("Salary - ", self.salary)    
# e1 = Employee("Ayushii", 22, 45000)
# e2 = Employee("Divya", 24, 55000)
# e1.display()
# e2.display()




# class Teacher:
#   def show(self):
#     print(" I AM A TEACHER - ")


# class Student:
#   def show(self):
#     print(" I AM A STUDENT - ") 


# class TeachingAssistant(Teacher , Student):
#   def display(self):
#     Teacher.show(self)
#     Student.show(self)

# ta = TeachingAssistant()
# ta.display()









































