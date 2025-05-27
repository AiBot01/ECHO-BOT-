
class Vehicle:
     def __init__(self,brand,model):
         self.brand = brand
         self. model = model


def start_engine(self):
    print(f"{self.brand} {self.model} engine started.")
    def stop_engine(self):
        print(f"{self.brand}{self.model}engine stopped.")

class Car(Vehicle):
    def __init__(self, brand, model , doors):
        super().__init__(brand, model)
        self.doors = doors

        def open_trunk(self):
            print(f"Opening the trunk of {self.brand}{self.model}. ")
def new_func():           
   my_car = Car("Toyota","corolla",4)

            my_car.start_engine()
            my_car.stop_engine()

            my_car.open_trunk()
            print(f"My car is a {my_car.model}with {my_car.doors} doors.")