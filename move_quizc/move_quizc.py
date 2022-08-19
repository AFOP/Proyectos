#!/usr/bin/python3
'''
move_quizc: object moves when answered correctly 
'''
from colorama import init, Fore, Back, Style
import os
import time

i = 0
speed = 0
form = "O^o"
print(Fore.YELLOW + "Welcome to the race Holberton 2022")
print("=============================================")
name = input(Fore.WHITE + "Name: ")
print("=============================================")
value = input(Fore.WHITE + "Please enter the speed of the bike: ")
print("=============================================")
value2 = int(value)
if (value2 > 15):
    value2 = 15
while (i < value2):
    os.system("clear")
    speed += i
    spaces = (" " * speed)
    street = ("= =" * 40)
    time.sleep(0.1)
    print(Fore.YELLOW + f"{street}" + Fore.RESET)
    print(Fore.BLUE + f"{spaces} {form} {Fore.RESET}")
    print(Fore.YELLOW + f"{street}" + Fore.RESET)
    i = i + 1

print(Fore.YELLOW+"Thanks for participate {:s} your speed is: {:s}".format(name, value))
