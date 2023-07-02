#Calma, Eugene Marie S.

from car_class import Car

class TestCar:
    def test (self):
        car = Car(1997, "Kia Pride", 0)
        #accelerate the car
        car.accelerate()
        car.accelerate()
        car.accelerate()
        car.accelerate()
        car.accelerate()
        car.brake()
        car.brake()
        car.brake()
        car.brake()
        car.brake()

        

test_run = TestCar()
test_run.test()