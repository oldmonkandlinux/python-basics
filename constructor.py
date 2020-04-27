'''
constructor
'''

class Zoo:
    def __init__(self,animal):
        self.animal = animal

    def talk(self):
        print("talk")

cat = Zoo("cat")
dog = Zoo("dog")
print(cat.animal)
cat.talk()
print(dog.animal)
dog.talk()
