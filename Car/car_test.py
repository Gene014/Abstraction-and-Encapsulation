#Calma, Eugene Marie S.

from car_class import Car

class TestCar:
    def test (self):
        car = Car(1997, "Kia Pride", 0)
        #accelerate the car
        for i in range (5):
            car.accelerate()

        for i in range (5):
            car.brake()
        

test_run = TestCar()
test_run.test()