class car:
    color="Black"
    @staticmethod
    def start():
        print("Car started..")

    @staticmethod
    def stop():
        print("Car stopped...")

class Toyotocar(car):
    def __init__(self , name):
        self.name=name

car1=Toyotocar("Fortune")
car2=Toyotocar("Hyundai")
print(car1.color) 