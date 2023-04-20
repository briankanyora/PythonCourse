from copyreg import pickle
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

pick = random.choice(names)

print(pick)


