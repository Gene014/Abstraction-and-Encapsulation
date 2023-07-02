#Calma, Eugene Marie S.
#carclass
class Car:
    def __init__(self,year_model,make,speed=0):
        self.__year_model = year_model
        self.__make = make
        self.__speed = speed
    
#getter and setter

    def get_year_model(self):
        return self.__year_model
    
    def set_year(self,year_model):
        self.__year_model = year_model

    def get_make(self):
        return self.__make
    
    def set_make(self, make):
        self.__make = make
    
    def set_speed(self, speed):
        self.__speed = speed
    
#acceleration method
    def accelerate(self):
        self.__speed += 5
        print(f'\33[31m*CAR ACCELERATING, BE CAREFUL!\33[31m*')
        print(f'\33[35mModel Year: {self.get_year_model()}')
        print(f'\33[35mCar Make: {self.get_make()}')
        print(f'\33[35mSpeed: {self.get_speed()} kp/h\n')

#braking system
    def brake (self):
        self.__speed -= 5
        print(f'\33[32m*SLOWING DOWN*\33[32m')
        print(f'\33[33mModel Year: {self.get_year_model()}')
        print(f'\33[33mCar Make: {self.get_make()}')
        print(f'\33[33mSpeed: {self.get_speed()} kp/h\n')
#return speed
    def get_speed(self):
        return self.__speed