#Calma, Eugene Marie S.

# creating class and getter setter
class Pet:
    def __init__(self,name,animal,age):
        self.__name = name
        self.__animal = animal
        self.__age = age
    def get_name(self):
        return self.__name
    def get_animal_type(self):
        return self.__animal
    def get_age(self):
        return self.__age 
    def set_name(self,name):
        self.__name = name
    def set_animal(self,animal_type):
        self.__animal = animal_type
    def set_age(self, age):
        self.__age = age
