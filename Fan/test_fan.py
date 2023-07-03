#Calma, Eugene Marie S.

#import fanfunc
from fan_functions import Fan
# test fan
# For the first object, assign the maximum speed, radius 10, color yellow, and turn it on. 
# Assign medium speed, radius 5, color blue, and turn it off for the second object. 

#fan1
class TestFan:
    def testrun (self):
        fan1 = Fan(Fan.MAX, True, 10, "yellow")
        # Display each object’s speed, radius, color, and on properties.
        print("\33[33mFan Speed:", fan1.get_speed())
        print("\33[35mFan Power", fan1.get_power())
        print("\33[33mFan Radius", fan1.get_radius())
        print("\33[35mFan Color", fan1.get_color())

#fan2
        fan2= Fan(Fan.MEDIUM,False, 5, "blue")
        # Display each object’s speed, radius, color, and on properties.
        print("\n\33[35mFan Speed:", fan2.get_speed())
        print("\33[33mFan Power", fan2.get_power())
        print("\33[35mFan Radius", fan2.get_radius())
        print("\33[33mFan Color", fan2.get_color())

#try the program first
test_fan = TestFan()
test_fan.testrun()