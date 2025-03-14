#OOP Exercise 1: Create a Class with instance attributes
class Vehicle:
    def __init__(self , max_speed , mileage):
        self.max_speed=max_speed
        self.mileage=mileage

model1= Vehicle(240 , 18)
print(model1.max_speed , model1.mileage)

#OOP Exercise 2: Create a Vehicle class without any variables and methods
class Vehicle:
    pass

#OOP Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Vehicle:
    def __init__(self , name, max_speed , mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(Vehicle):
    pass

school_bus=Bus("School Caliber convent school" , 180 , 12)
print("Vehicle Name:" , school_bus.name , "Speed:" , school_bus.max_speed, "Mileage:" , school_bus.mileage)


#OOP Exercise 4: Class Inheritance
class Vehicle:
    def __init__(self , name , max_speed , mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

    def seating_capacity(self , capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)
    
school_bus=Bus("School caliber" , 180 , 12)
print(school_bus.seating_capacity())

#OOP Exercise 5: Define a property that must have the same value for every class instance (object)
#Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

class Vehicle:
    color="White"

    def __init__(self , name , max_speed , mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

school_bus=Bus("School Volvo" , 180 , 12)
print(school_bus.color , school_bus.name , "Speed:" , school_bus.max_speed , "Mileage:" , school_bus.mileage)

car= Car("Audi Q5" , 250 , 18)
print(car.color , car.name , "Speed:" , car.max_speed , "Mileage:" , car.mileage)

#OP Exercise 6: Class Inheritance
#Given:

#Create a Bus child class that inherits from the Vehicle class.
 #The default fare charge of any vehicle is seating capacity * 100. 
 #If Vehicle is Bus instance, we need to add an extra 10% on full 
 #fare as a maintenance charge. So total fare for bus instance will
 #become the final amount = total fare + 10% of the total fare.

class Vehicle:
    def __init__(self , name , mileage , capacity):
        self.name=name
        self.mileage=mileage
        self.capacity=capacity

    def fare(self):
        return self.capacity* 100
    
class Bus(Vehicle):
    def fare(self):
        amount=super().fare()
        amount+= amount * 10/ 100
        return amount
    
school_bus=Bus("School Volvo " , 12 , 50)
print("Total Bus fare is:" , school_bus.fare())

#OOP Exercise 7: Check type of an object
class Vehicle:
    def __init__(self , name , mileage , capacity):
        self.name=name
        self.mileage=mileage
        self.capacity=capacity

class Bus(Vehicle):
    pass

school_bus=Bus("School Volvo " , 12, 50)

print(type(school_bus))


#OOP Exercise 8: Determine if School_bus is also an instance of the Vehicle class
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

print(isinstance(school_bus , Vehicle))

