from abc import ABC, abstractmethod


class Robot(ABC):
    def __init__(self, name, model, power_level=100):
        self.name = name
        self.model = model
        self.power_level = power_level

    def showInfo(self):
        print(f"Name: {self.name}, model: {self.model}, power: {self.power_level}")

    @abstractmethod
    def perform_task(self):
        pass

    def charge(self,tmp):
        self.power_level=min(100,self.power_level+tmp)
        print(f"Charging,now power is {self.power_level}")


class WorkerRobot(Robot):
    def __init__(self, name, model,tool, power_level=100, file="undefinded"):
        super().__init__(name, model, power_level)
        self.tool = tool
        self.file=file

    def perform_task(self):
        self.power_level -= 10
        if self.power_level <=0:
            print("You don't have energy,you have to charge")
        else:
            print(f"Name: {self.name}, model: {self.model}, power: {self.power_level}, tool: {self.tool}")

    def __enter__(self):
        self.file=open(self.file,"w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()


class DefenseRobot(Robot):
    def __init__(self, name, model, weapon, power_level=100):
        super().__init__(name, model, power_level)
        self.weapon = weapon

    def perform_task(self):
        self.power_level -= 15
        if self.power_level <=0:
            print("You don't have energy,you have to charge")
        else:
            print(f"Name: {self.name}, model: {self.model}, power: {self.power_level}, weapon: {self.weapon}")

    def __del__(self):
        print("об'єкт очищено")


class ServiceRobot(Robot):
    def __init__(self, name, model, service_type, power_level=100):
        super().__init__(name, model, power_level)
        self.service_type = service_type

    def perform_task(self):
        self.power_level -= 5
        if self.power_level <= 0:
            print("You don't have energy,you have to charge")
        else:
            print(f"Name: {self.name}, model: {self.model}, power: {self.power_level}, service_type: {self.service_type}")

    def __del__(self):
        print("об'єкт очищено")


obj1 = WorkerRobot("Bob", "X1", "Wrench")
int=str(obj1.power_level)
with WorkerRobot("Bob", "X1", "Wrench",100,"Myfile.txt") as fl:
    fl.write(obj1.name)
    fl.write(int)
obj2 = DefenseRobot("Defender", "Z3", "Laser")
obj3 = ServiceRobot("Helper", "S2", "Cleaning")
obj1.showInfo()
obj1.perform_task()
obj1.charge(9)
obj1.perform_task()
obj1.perform_task()
print("")
obj2.showInfo()
obj2.perform_task()
obj2.charge(1)
obj2.perform_task()
obj2.perform_task()
print("")
obj3.showInfo()
obj3.perform_task()
obj3.charge(900)
obj3.perform_task()
obj3.perform_task()