class person:
    name="Sanika"
    @classmethod
    def changeName(cls , name):
        cls.name=name

p1=person()
p1.changeName("Sakshi Salunkhe")
print(p1.name)
print(person.name)