#runtime polymorphism

class Animal:
    def sound(self):
        return 'Some sound'

class Dog(Animal):
    def sound(self):
        return 'Bark'

obj = Dog()
print(obj.sound())