class car:
    @staticmethod
    def start():
        print("Car started")

    @staticmethod
    def stop():
        print("Car stopped")

class Toyotocar(car):
    def __init__(self , brand):
        self.brand=brand

class fortuner(Toyotocar):
    def __init__(self, type):
        self.type=type

car1=fortuner("Diesel")
car1.start()