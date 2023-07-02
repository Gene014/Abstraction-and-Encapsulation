from pet_class import Pet
from pet_testrun import PetTest


#testrun the code
test_run = PetTest
test_run.userint()
while True:
    askyesno = input("\n\33[46mDo you still want to continue? (yes/no):\33[0m ")
    if askyesno.lower() == 'no':
        print("\33[41mTerminating Program... ")
        exit()
    elif askyesno.lower() == 'yes':
        continue
    else:
        raise TypeError