'''
lists in python and some list functions
'''
names = ["ram", "shyam", "ghanshyam", "laxman"]

names.reverse()
names.append("sita")
names.append("sita")
names.pop(4)

print(names.count("sita"))
print(names)

names.insert(5,"rita")
names_second = names.copy()
print(names)
print(names_second)
