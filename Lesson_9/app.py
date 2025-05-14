# OOP (Object Oriented Programming)

# Classes

# class Dog:
# """A class to represents dogs"""

# def __init__(self, name, age, gender, breed):
#     self.name = name
#     self.age = age
#     self.gender = gender
#     self.breed = breed

# def describe_dog(self):
#     print(
#         f"Dog Name: {self.name}, Dog Age: {self.age}, Dog Gender: {self.gender[0]}, Dog Breed: {self.breed}")

# def sit_dog(self):
#     print(f"{self.name} is sitting")

# def dog_sprint(self):
#     print(f"{self.name} is sprinting")


# precious_dog = Dog("Lucy", 5, "Male", "German Shepard")
# efe_dog = Dog("Daisy", 2, "Female", "German Shepard")

# print(precious_dog.name)
# print(efe_dog.name)

# precious_dog.describe_dog()
# efe_dog.describe_dog()

# precious_dog.sit_dog()
# precious_dog.dog_sprint()

# Assignment a class to represent Cars and pass the (name, year, model, brand)
# Create a method to describe the car
# Create a Dictionary to to hold the fuel guage and create a method to print out the fuel guages. {"full": 100, "Half": 50, "Empty": 10}
# Create a variable to hold the car millage then create two methods to get the current car millge and to add to the car millage
# Create an instance of the class and print out the description of the car
# Use that instance to print out the name of the car and use the instance to call the methods you created in the Car class

# Assignment 2
# Create a class to represent students we have at coriftech
# Pass information about the students
# Create a method to print out the information of the student
# Create a List showing the courses the students are offering
# Create two methods to get all the courses the students are offering and the second method to add to courses
# Create an instance of the class and print out the description of the Student
# Use that instance to print out the name of the student and use the instance to call the methods you created in the Student class


# class Student:
#     """A class to model the students we have at Coriftech"""

#     # A constructor
#     def __init__(self, full_name, age, gender):
#         """This init function is called first on every run"""
#         self.full_name = full_name
#         self.age = age
#         self.gender = gender
#         self.course = ["Graphics", "Software", "Data Analysis"]

#     def describe_student(self):
#         """We print out the infor of the students"""
#         print(f"Name: {self.full_name}, Age: {self.age}, Gender: {self.gender}")

#     def get_courses(self):
#         """We are getting the courses the students are offering"""
#         print(", ".join(self.course))

#     def add_course(self, *new_course):
#         """We are adding to the courses the students are offering"""
#         self.course += list(new_course)

#     # Assignment: Remove more than one course from the self.course list
#     def remove_course(self, course_name):
#         first, second = course_name
#         self.course.remove(first)
#         self.course.remove(second)


# student1 = Student("Emma EfeOgene", 27, "Male")
# # student2 = Student("Efe", 23, "Male")

# # student1.get_courses()
# student1.add_course("Msword", "Excel", "Powerpoint")
# student1.get_courses()
# student1.remove_course(["Msword", "Excel"])
# student1.get_courses()

# class Animals:
#     # Doc String
#     """A class to hold the generic property of Animals"""
#     # Class Attribute
#     breathe = "All animals can breathe"

#     # Constructor: Runs immediately the class is run
#     def __init__(self, name):
#         """A constructor to initialize the name of the animal"""
#         # Instant Attribute
#         self.name = name

#     def describe_animal(self):
#         """A method to describe the animal"""
#         print(f"This animal is a {self.name}")


# class Bird(Animals):
#     """A class to hold properties of bird"""

#     def __init__(self, name):
#         super().__init__(name)
#         self.fly = "fly"

#     def bird_property(self):
#         print(f"Only {self.name} {self.fly}")


# class Fish(Animals):
#     """A class to hold properties of fish"""

#     def __init__(self, name):
#         super().__init__(name)
#         self.swim = "swim"

#     def fish_property(self):
#         print(f"Only {self.name} {self.swim}")


# class Lion(Animals):
#     """A class to hold properties of lions"""

#     def __init__(self, name):
#         super().__init__(name)
#         self.roar = "roar"

#     def lion_property(self):
#         print(f"Only {self.name} {self.roar}")


# bird = Bird("Bird")
# fish = Fish("Fish")
# lion = Lion("Lion")

# print("Printing the names of all the animals")
# print(bird.name)
# print(fish.name)
# print(lion.name)

# print("\nPrinting properties of all the animals")
# bird.describe_animal()
# fish.describe_animal()
# lion.describe_animal()

# print("\nPrinting properties of individual animal")
# bird.bird_property()
# fish.fish_property()
# lion.lion_property()

# Assignment:
# Create an Car class and give it generic properties of cars ****
# Create a method inside the car class to print out the description of the car***
# Create two new classes for electric cars and petrol cars and make them inherit from Car properties *****
# Create specific functions for the individual classes
# Create an instance of the electric car and the petrol car and call the describe car method with the two instances
# Call the specific methods for the electric car and petrol car

# Abstraction
# from abc import ABC, abstractmethod

# # Parent or Base class


# class Car(ABC):
#     """Car class representing a Car"""

#     def __init__(self, brand, year, model):
#         self.brand = brand
#         self.year = year
#         self.model = model
#         self.millage = 0

#     def car_description(self):
#         print(
#             f"Car Name: {self.brand}, Car Year: {self.year}, Car Model: {self.model}")

#     @abstractmethod
#     def drive_car(self, distance):
#         if distance < 0:
#             print("Distance cannot be negative")
#         self.millage += distance

# # Child class or sub class


# class ElectricCar(Car):
#     """Electric car model"""

#     def __init__(self, brand, year, model):
#         super().__init__(brand, year, model)
#         self.battery_capacity = 70

#     def get_battery_capacity(self):
#         return self.battery_capacity

#     def drive_car(self, distance):
#         return super().drive_car(distance)


# class PetrolCar(Car):
#     """Petrol car model"""

#     def __init__(self, brand, year, model):
#         super().__init__(brand, year, model)
#         self.fuel_guage = {70: "Full", 50: "Half", 30: "Low", 10: "Empty"}
#         self.fuel = 100

#     def get_fuel_guage(self):
#         value = list(
#             {guage for guage in self.fuel_guage if guage <= self.fuel})
#         value.sort(reverse=True)
#         return self.fuel_guage.get(value[0], "")

#     def drive_car(self, distance):
#         self.fuel -= distance/2
#         return super().drive_car(distance)


# lexus = PetrolCar("Toyota", 2026, "GX470")
# # tesla = ElectricCar("Tesla", 2025, "TeslaX")

# lexus.car_description()
# lexus.drive_car(100)
# lexus.drive_car(25)
# lexus.drive_car(20)
# print(lexus.fuel)
# print(lexus.get_fuel_guage())
# print(lexus.millage)
