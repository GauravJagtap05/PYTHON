
# Implement the following Manager class with getter and setter methods.
# class Manager:
# # id, name, deptname, salary, gender (M or F)

# class Manager:
#     def __init__(self):
#         self.id = 123
#         self.name = 'Ramesh'
#         self.deptname = 'Data'
#         self.salary = 20000000
#         self.gender = 'M'
#
#     def setid(self):
#         self.id
#     def getid(self):
#         return self.id
#
#     def setname(self):
#         self.name
#     def getname(self):
#         return self.name
#
#     def setdeptname(self):
#         self.deptname
#     def getdeptname(self):
#         return self.deptname
#
#     def setsalary(self):
#         self.salary
#     def getsalary(self):
#         return self.salary
#
#     def setgender(self):
#         self.gender
#     def getgender(self):
#         return self.gender
#
# m = Manager()
# print("id ",m.getid())
# print("name",m.getname())
# print("deptname ",m.getdeptname())
# print("salary ",m.getsalary())
# print("gender ",m.getgender())


    # def __init__(self):
    #     self.id = 123
    #     self.name = 'Ramesh'
    #     self.deptname = 'Data'
    #     self.salary = 20000000
    #     self.gender = 'M'

# with taking the input  -------------------------------------------

# class Manager:
#     def setid(self):
#         self.id = int(input("enter the manager id : ", ))
#     def getid(self):
#         return self.id
#
#     def setname(self):
#         self.name= str(input("enter the manager name : ", ))
#     def getname(self):
#         return self.name
#
#     def setdeptname(self):
#         self.deptname = str(input("enter the manager dept : ", ))
#     def getdeptname(self):
#         return self.deptname
#
#     def setsalary(self):
#         self.salary = int(input("enter the manager salary : ", ))
#     def getsalary(self):
#         return self.salary
#
#     def setgender(self):
#         self.gender = str(input("enter the manager gender : ", ))
#     def getgender(self):
#         return self.gender
#
#
# m = Manager()
# m.setid()
# m.setname()
# m.setdeptname()
# m.setsalary()
# m.setgender()
# print(m.getid())
# print(m.getname())
# print(m.getdeptname())
# print(m.getsalary())
# print(m.getgender())


# 37. Write a static method that accepts a number and returns its factorial value.
#
# class factorial:
#
#     @staticmethod
#     def fact_num(x):
#         result =1
#         for i in range(1, x+1):
#             result *= i
#         return result
#
# num = int(input(" enter the number : "))
# print(factorial.fact_num(num))
#

# 35. What is a nested class and what is its advantage?

# class inside the other class is nested class


# 36. What is name mangling? How can you implement it?


# class with a method that accepts the number of sides using inputSides() method.
# Derive Traingle class from Polygon class.Write area() method in the Traingle class.
# Create an object to Triangle class and call the inputSides() and pass number of sides as 3.
# Then display area of traingle by calling area().

#
# class Polygon:
#     def input_sides(self,sides):
#         self.sides = sides
#
# class traingle(Polygon):
#
#     def area_triangle( self , base, height):
#         result = 0.5 * base * height
#         return result
# 
# obj = traingle()
# obj.input_sides(3)
# base = int(input(" enter the base : "))
# height = int(input(" enter the height : "))
# print(obj.area_triangle(base, height))



