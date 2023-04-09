class Base:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def getSex(self):
        return self.age
    

class Person(Base):
    def __init__(self, name, age):
        super().__init__(name, age)

    def getName(self):
        return self.name
    

person = Person('张三', 18)
print(person.getName())
print(person.getSex())
    
    