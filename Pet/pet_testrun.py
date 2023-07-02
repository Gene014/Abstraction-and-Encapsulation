#Calma, Eugene Marie S.
from pet_class import Pet

#create testrun
class PetTest:
    def userint():
        name = input("Good Day! Please Enter the name of your Pet.")
        animal_type = input ("Please Enter the type or breed of your Pet.")
        age = input ("Please Enter the age of your Pet.")
        pet = Pet(name, animal_type, age)
#print pet informations
        print(f'Your Pet name is{pet.get_name()}.')
        print(f'Your pet is {pet.get_animal_type()}.')
        print(f'The age of your pet is {pet.get_age()} years old.')      