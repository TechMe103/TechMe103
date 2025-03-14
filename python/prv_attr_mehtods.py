class person:
    __name="Sanika"
    def __hello(self):
        print("Hello")
    def welcome(self):
        self.__hello()
p1=person()
print(p1.welcome())