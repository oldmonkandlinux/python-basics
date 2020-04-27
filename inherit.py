class Animal:
    def walk(self):
        print("walk")


class Dog(Animal):
    pass

class Cat(Animal):
    def annoying(self):
        print("cats are annoying")


tom = Dog()
tom.walk()

bruno = Cat()
bruno.walk()
bruno.annoying()

