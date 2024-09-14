class Appliance:
    def __init__(self,brand ):
        self.brand =brand
    def get_info(self):
        print(f"brand: {self.brand}")

class KitchenAppliance(Appliance):
    def __init__(self,brand,power):
        super().__init__(brand)
        self.power=power
    def get_info(self):
        super().get_info()
        print(f"power: {self.power}")

class Oven(KitchenAppliance):
    def __init__(self,brand,power,temperature_range ):
        super().__init__(brand,power)
        self.temperature_range=temperature_range
    def get_info(self):
        super().get_info()
        print(f"temperature_range: {self.temperature_range}")

class Microwave(KitchenAppliance):
    def __init__(self,brand,power,capacity):
        super().__init__(brand,power)
        self.capacity=capacity
    def get_info(self):
        super().get_info()
        print(f"capacity: {self.capacity}")

obj1=Oven("phenix",3000,180)
obj2=Microwave("mik",1500,"medium")
obj1.get_info()
obj2.get_info()




