import random

names_str = input("enter names seperated by commas:")
names = names_str.split(",")
num_items= len(names)
random_select = random.randint(0,len(names))
person_paying = names[random_select]
print(f"{person_paying} is paying the bill")