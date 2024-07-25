# This is a sample Python script.

import os
print("Welcome to robospeaker 1.1 \nCREATED BY SHIVENDRA")
while True:
    X = input("Enter what you want me to speak: ")
    if X == "z":
        #os.system("bye bye freind")
        break
    command = f" say {X}"
    os.system(command)


