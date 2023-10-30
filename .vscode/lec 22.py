#lab 21 

###########################################
# # Object oriented Programming Concept
# # creating phone class
# class Phone:
#     def make_call(self):
#         print("Make Phone Call")

#     def play_game(self):
#         print("Play Game")
# # initializing the "p1" object create
# p1 = Phone()

# # Invoking methods through objects
# p1.make_call()
# p1.play_game()





####################################################
# # Second Approach
# # setting and returning the attributive values
# class Phone:
#     def set_color(self,color):
#         self.color = color
#     def set_cost(self,cost):
#         self.cost = cost
#     def show_color(self):
#         return self.color
#     def show_cost(self):
#         return self.cost
#     def make_call(self):
#         print("Make Phone Call")
#     def play_game(self):
#         print("Play Game")

# p2 = Phone()
# p2.set_color("blue")
# p2.set_cost(300)

# print(p2.show_color())
# print(p2.show_cost())
# p2.make_call()
# p2.play_game()

#################################################
# third approach init methos acts as a constructor
# class Employee:
#     def __init__(self,name,age,salary,gender):
#         self.name = name
#         self.age = age
#         self.salary = salary
#         self.gender = gender

#     def show_employee_details(self):
#         print("Name of Employee is ",self.name)
#         print("Age of employee is ",self.age)
#         print("Slary of employee is ",self.salary)
#         print("Gender of employee is",self.gender)

# e1 = Employee('Meet',25,30000,'Male')
# e1.show_employee_details()


############################################

# Example regarding inheritance in python (inehritance)
# Creating the base class

class Vehicle:
    def __init__(self,mileage,cost):
        self.mileage = mileage
        self.cost = cost
    def show_details(self):
        print("\n Vehicle")
        print("Mileage of Vehicle is ", self.mileage)
        print("Cost of Vehicle is ",self.cost)

v1 = Vehicle(50,50000)
v1.show_details()


# # creating child class
class Car(Vehicle):
    def show_car(self):
        print("\n Car")
# Instantiating the object for child class
c1 = Car(20,20000)
c1.show_details()
# invoking the child class method
c1.show_car()




# creating child class
class Car(Vehicle):
# Example Over-riding init method
    def __init__(self,mileage,cost,types,horse_power):
        super().__init__(mileage,cost)
        self.types = types
        self.horse_power = horse_power

    def show_car_details(self):
        print("\n CaAr")
        print("Numbers of types are ", self.types)
        print("Value of Horse Power is ",self.horse_power)
# Instantiating the object for child class
c1 = Car(20,2000,4,200)
# invoking the parent class method
c1.show_details()
# invoking the child class method
c1.show_car_details()

