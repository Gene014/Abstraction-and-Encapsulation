#Calma, Eugene Marie S.
#(The Fan class).  Design a class named Fan to represent a fan. The class contains:
# Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
# ■ A private int data field named speed that specifies the speed of the fan.
#■ A private bool data field named on that specifies whether the fan is on (the default is False).
#■ A private float data field named radius that specifies the radius of the fan.
#■ A private string data field named color that specifies the color of the fan.
#■ The accessor(getters)  and mutator(setters)  methods for all four data fields.
#■ A constructor that creates a fan with the specified speed (default SLOW), radius (default 5), color (default blue), and on (default False).
#Write a test program named TestFan that creates two Fan objects. For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. Assign medium speed, radius 5, color blue, and turn it off for the second object. Display each object’s speed, radius, color, and on properties.

class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self,speed=1,power=False,radius=5,color="blue"):
        self.__speed = speed
        self.__power = power
        self.__radius = float (radius)
        self.__color = color
    
    def get_speed(self):
        return self.__speed

    def set_speed(self):
        self.__speed

    def get_power(self):
        if self.__power == True:
            condition = "On"
        else:
            condition = "Off"
        return condition
    
    def set_power(self, power):
        self.__power = power
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, radius):
        self.__radius = radius

    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color