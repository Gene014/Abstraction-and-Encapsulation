#Calma, Eugene Marie S.

#import fanfunc
from fan_functions import Fan
# test fan
# For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. 
# Assign medium speed, radius 5, color blue, and turn it off for the second object. 

class TestFan:
    def testrun (self):
        fan1 = Fan(Fan.SLOW, True, 10, "yellow")
        # Display each object’s speed, radius, color, and on properties.
        print("Fan Speed:", fan1.get_speed())
        print("Fan Power", fan1.get_power())
        print("Fan Radius", fan1.get_radius())
        print("Fan Color", fan1.get_color())

#try the program first
test_fan = TestFan()
test_fan.testrun()