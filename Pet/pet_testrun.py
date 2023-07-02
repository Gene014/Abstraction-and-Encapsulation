#Calma, Eugene Marie S.
from pet_class import Pet

#create testrun
class PetTest:
    def userint():
        name = input("\33[33mGood Day! Please Enter the name of your Pet.")
        animal_type = input ("\33[35mPlease Enter the type or breed of your Pet.")
        age = input ("\33[34mPlease Enter the age of your Pet.")
        pet = Pet(name, animal_type, age)
#print pet informations
        print(f'\n\33[33mYour Pet name is{pet.get_name()}.')
        print(f'\n\33[35mYour pet is {pet.get_animal_type()}.')
        print(f'\n\33[34mThe age of your pet is {pet.get_age()} years old.')      