'''
demonstrates class and objects
'''
class Zoo:
    def cat(self):
        print("Meow")
    def horse(self):
        print("neigh neigh")

speak = Zoo()
speak.cat()
speak.horse()
print("----------")

speak_again = Zoo()
speak_again.horse()
speak_again.cat()